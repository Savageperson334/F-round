"""The smoothie: one program made of other people's functions.

Give it a seed. It hands the seed to a real function copied from some
repository, hands what comes back to a function from a different repository,
and keeps going for as long as real calls keep succeeding. Every link it uses
was found by trying it (see CONNECTIONS.md); the seed decides the route.

    python blender/smoothie.py "moth"
    python blender/smoothie.py 440 --steps 30
    python blender/smoothie.py --recipe 0        replay one of the long chains found
    python blender/smoothie.py --list            what is in the blend

It prints the trail and writes three files to blender/out/: the trail as
text, a drawing of it (SVG) and the sound of it (WAV). The drawing and the
sound are this program's own renderings of the numbers that went past.

The functions in berries/ are other people's code, copied verbatim; CREDITS.md
names every repository. The blend as a whole is under the GNU GPL v3 or later.

Python is all it needs. With numpy installed the numpy functions join in, and
with Node installed the JavaScript ones do; without them those are skipped.
"""
import argparse
import contextlib
import importlib
import io
import json
import math
import os
import random
import re
import struct
import sys
import threading
import time
import wave

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sandbox  # noqa: E402
from sandbox import FITS, kind, tame  # noqa: E402

STEP_SECONDS = 3.0
MAP = json.load(open(os.path.join(HERE, "blend_map.json"), encoding="utf-8"))
FUNCTIONS = MAP["functions"]
EDGES = MAP["edges"]
_loaded = {}
_quiet = io.StringIO()
BRIDGE = sandbox.NodeBridge(timeout_ms=2000)
HAVE_NUMPY = sandbox.numpy_allowed() is not None
HAVE_NODE = __import__("shutil").which("node") is not None


def available(fid):
    info = FUNCTIONS[str(fid)]
    return HAVE_NODE if info["lang"] == "js" else (HAVE_NUMPY or not info["numpy"])


def berry(fid):
    """The real function: imported from its file in berries/, or handed to Node if it is JavaScript."""
    if fid not in _loaded:
        info = FUNCTIONS[str(fid)]
        if info["lang"] == "js":
            code = open(os.path.join(HERE, "berries", info["module"] + ".js"), encoding="utf-8").read()
            _loaded[fid] = BRIDGE.function(fid, info["name"], code)
        else:
            with contextlib.redirect_stdout(_quiet):
                fn = getattr(importlib.import_module("berries." + info["module"]), info["name"])
            _loaded[fid] = sandbox.wrap(fn, info["numpy"])
    return _loaded[fid]


class Watch:
    """Stops the whole run if one borrowed function will not come back."""

    def __init__(self):
        self.current, self.since = None, 0.0
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        while True:
            time.sleep(0.25)
            if self.current is not None and time.time() - self.since > STEP_SECONDS:
                info = FUNCTIONS[str(self.current)]
                print("\n%s (from %s) did not come back within %.0f seconds. Stopping." % (info["name"], info["repo"], STEP_SECONDS))
                os._exit(2)


WATCH = Watch()


def call(fid, pos, fixed, value):
    """One real call: `value` in position `pos`, the other arguments as found when the link was tested."""
    if not available(fid):
        return False, None
    if isinstance(fixed, int):
        fixed = FUNCTIONS[str(fid)]["fixed"][fixed]
    args = json.loads(json.dumps(fixed))
    args[pos] = json.loads(json.dumps(value))
    WATCH.current, WATCH.since = fid, time.time()
    try:
        with contextlib.redirect_stdout(_quiet):   # some borrowed functions print as they go
            result = berry(fid)(*args)
    except Exception:  # noqa: BLE001
        return False, None
    finally:
        WATCH.current = None
        _quiet.seek(0)
        _quiet.truncate()
    if result is None or not tame(result):
        return False, None
    if isinstance(result, int) and not isinstance(result, bool) and abs(result) > 10 ** 7:
        return False, None
    if isinstance(result, float) and abs(result) > 1e12:
        return False, None
    if kind(result) not in FITS:
        return False, None
    try:
        return True, json.loads(json.dumps(result))
    except (TypeError, ValueError):
        return False, None


def blend(seed, steps, rng):
    """Walk from the seed through real functions for as long as calls succeed."""
    starters = []
    for fid, info in FUNCTIONS.items():
        for start in info["starts"]:
            if start["kind"] in FITS.get(kind(seed), ()):
                starters.append((int(fid), start["fixed"]))
    rng.shuffle(starters)
    trail = []
    starters.sort(key=lambda s: FUNCTIONS[str(s[0])]["wrapper"])   # wrappers last
    for fid, fixed in starters[:60]:
        ok, value = call(fid, 0, fixed, seed)
        if ok and str(fid) in EDGES:
            trail.append({"f": fid, "named": False, "value": value})
            break
    if not trail:
        return trail
    used = {trail[0]["f"]}
    repos = {FUNCTIONS[str(trail[0]["f"])]["repo"]}
    shelves = {FUNCTIONS[str(trail[0]["f"])]["shelf"]}
    while len(trail) < steps:
        options = [e for e in EDGES.get(str(trail[-1]["f"]), []) if e[0] not in used and available(e[0])]
        if not options:
            break
        here = FUNCTIONS[str(trail[-1]["f"])]["lang"]
        weights = []
        for e in options:
            g = FUNCTIONS[str(e[0])]
            # Prefer links by name, new fields, new repositories, a change of language and numpy code;
            # avoid functions that only wrap what they are given in a labelled box.
            weights.append((6.0 if e[3] else 1.0) * (3.0 if g["shelf"] not in shelves else 1.0)
                           * (2.0 if g["repo"] not in repos else 0.5) * (2.0 if g["lang"] != here else 1.0)
                           * (3.0 if g["numpy"] else 1.0) * (0.03 if g["wrapper"] else 1.0))
        moved = False
        for attempt in range(12):
            g, pos, fixed, named, token = rng.choices(options, weights)[0]
            ok, result = call(g, pos, fixed, trail[-1]["value"])
            if ok and result != trail[-1]["value"]:
                trail.append({"f": g, "named": bool(named), "token": token, "value": result})
                used.add(g)
                repos.add(FUNCTIONS[str(g)]["repo"])
                shelves.add(FUNCTIONS[str(g)]["shelf"])
                moved = True
                break
        if not moved:
            break
    return trail


def replay(recipe):
    trail, value = [], recipe["seed"]
    for fid, pos, fixed, named in recipe["steps"]:
        ok, value = call(fid, pos, fixed, value)
        if not ok:
            break
        trail.append({"f": fid, "named": named, "value": value})
    return trail


# ------------------------------------------------------------ renderings
# Everything below is this program's own code, not borrowed.

def numbers_in(value):
    if isinstance(value, bool):
        return [1.0 if value else 0.0]
    if isinstance(value, (int, float)):
        return [float(value)]
    if isinstance(value, str):
        return [float(ord(c)) for c in value[:64]]
    if isinstance(value, (list, tuple)):
        out = []
        for v in value:
            out += numbers_in(v)
        return out[:64]
    if isinstance(value, dict):
        return numbers_in(list(value.values()))
    return []


def squash(x):
    """Any number to 0..1, keeping order: sign-aware log scale."""
    return 0.5 + math.atan(math.copysign(math.log1p(abs(x)), x) / 3.0) / math.pi


def show(value):
    text = json.dumps(value, ensure_ascii=False)
    return text if len(text) <= 78 else text[:75] + "..."


def write_text(path, seed, trail):
    lines = ["seed: %s" % show(seed), ""]
    for i, step in enumerate(trail):
        info = FUNCTIONS[str(step["f"])]
        link = "by name (%s)" % step.get("token", "") if step["named"] else ("start" if i == 0 else "by shape")
        lines.append("%2d. %s  ->  %s" % (i + 1, info["name"], show(step["value"])))
        lines.append("    %s  %s:%d  [%s]  shelf: %s  link: %s" % (info["url"], info["file"], info["line"], info["licence"], info["shelf"], link))
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")


def write_svg(path, seed, trail):
    width, row = 900, 30
    height = 70 + row * len(trail)
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" font-family="monospace" font-size="11">' % (width, height),
             '<rect width="100%" height="100%" fill="#101116"/>',
             '<text x="14" y="24" fill="#b8ff8f" font-size="14">seed %s through %d real functions</text>' % (
                 show(seed).replace("&", "&amp;").replace("<", "&lt;"), len(trail))]
    previous = None
    for i, step in enumerate(trail):
        info = FUNCTIONS[str(step["f"])]
        y = 60 + row * i
        values = numbers_in(step["value"]) or [0.0]
        xs = [380 + 500 * squash(v) for v in values]
        colour = "#b8ff8f" if step["named"] else "#d6adff"
        points = " ".join("%.1f,%.1f" % (x, y - 8 + 16 * (j / max(1, len(xs) - 1))) for j, x in enumerate(xs))
        if len(xs) > 1:
            parts.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.2"/>' % (points, colour))
        for x in xs[:1]:
            parts.append('<circle cx="%.1f" cy="%d" r="3" fill="%s"/>' % (x, y, colour))
        if previous is not None:
            parts.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#555a66" stroke-width="0.8"/>' % (previous[0], previous[1], xs[0], y))
        previous = (xs[0], y)
        label = "%s  %s" % (info["name"], info["repo"])
        parts.append('<text x="14" y="%d" fill="#c2c7ce">%s</text>' % (y + 4, label[:56].replace("&", "&amp;").replace("<", "&lt;")))
    parts.append("</svg>")
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(parts))


def write_wav(path, trail):
    rate, frames = 11025, bytearray()
    for step in trail:
        values = (numbers_in(step["value"]) or [0.0])[:6]
        length = int(rate * 0.22 / len(values)) or 1
        for v in values:
            freq = 110.0 * (2.0 ** (4.0 * squash(v)))
            for n in range(length):
                envelope = min(1.0, n / 60.0) * min(1.0, (length - n) / 60.0)
                sample = 0.45 * envelope * (math.sin(2 * math.pi * freq * n / rate) + 0.3 * math.sin(4 * math.pi * freq * n / rate))
                frames += struct.pack("<h", int(max(-1.0, min(1.0, sample)) * 30000))
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(bytes(frames))


def parse_seed(text):
    try:
        return json.loads(text)
    except (TypeError, ValueError):
        return text


def main():
    parser = argparse.ArgumentParser(description="One program made of other people's functions.")
    parser.add_argument("seed", nargs="?", default="f-round", help="text, a number, or a JSON list of numbers")
    parser.add_argument("--steps", type=int, default=24)
    parser.add_argument("--recipe", type=int, default=None, help="replay long chain number N")
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()
    if args.list:
        repos = sorted({f["repo"] for f in FUNCTIONS.values()})
        print("%d real functions from %d repositories; %d tested links; %d long chains stored" % (
            len(FUNCTIONS), len(repos), sum(len(v) for v in EDGES.values()), len(MAP["recipes"])))
        print("  Python %d (of which numpy %d, %s), JavaScript %d (%s)" % (
            sum(1 for f in FUNCTIONS.values() if f["lang"] == "py"), sum(1 for f in FUNCTIONS.values() if f["numpy"]),
            "numpy found" if HAVE_NUMPY else "numpy NOT installed: skipped",
            sum(1 for f in FUNCTIONS.values() if f["lang"] == "js"), "Node found" if HAVE_NODE else "Node NOT installed: skipped"))
        return
    if args.recipe is not None:
        recipe = MAP["recipes"][args.recipe]
        seed, trail = recipe["seed"], replay(recipe)
    else:
        seed = parse_seed(args.seed)
        trail = blend(seed, args.steps, random.Random(json.dumps(seed)))
    if not trail:
        print("Nothing in the blend would take %s." % show(seed))
        return
    repos = {FUNCTIONS[str(s["f"])]["repo"] for s in trail}
    shelves = {FUNCTIONS[str(s["f"])]["shelf"] for s in trail}
    print("seed %s" % show(seed))
    for i, step in enumerate(trail):
        info = FUNCTIONS[str(step["f"])]
        mark = "=" if step["named"] else "-"
        tongue = "js" if info["lang"] == "js" else ("np" if info["numpy"] else "py")
        print("%2d %s %s %-30s %-40s %s" % (i + 1, mark, tongue, info["name"][:30], info["repo"][:40], show(step["value"])[:60]))
    print("\n%d real functions from %d repositories on %d shelves (= fits by name, - fits by shape; py Python, np numpy, js JavaScript)" % (
        len(trail), len(repos), len(shelves)))
    out = os.path.join(HERE, "out")
    os.makedirs(out, exist_ok=True)
    base = os.path.join(out, re.sub(r"[^A-Za-z0-9]+", "_", str(args.seed if args.recipe is None else "recipe_%d" % args.recipe)).strip("_")[:40] or "seed")
    write_text(base + ".txt", seed, trail)
    write_svg(base + ".svg", seed, trail)
    write_wav(base + ".wav", trail)
    print("wrote %s.txt, .svg and .wav" % os.path.relpath(base, os.getcwd()))
    BRIDGE.close()


if __name__ == "__main__":
    main()
