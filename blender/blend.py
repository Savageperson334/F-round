"""The blend: which real functions, from different repositories, feed each other.

For every pair (f, g) of harvested functions from DIFFERENT repositories, where
the shape f returns is one g ran on when probed, this feeds f's real outputs
into g and keeps the pair only if g really runs on them and its answers change
when f's do. Most pairs fail. What is left is the map of real code, written by
strangers for unrelated purposes, that actually connects.

Then it goes looking for long chains: starting from a plain seed, pass the
value from function to function for as long as real calls keep succeeding,
favouring chains that cross the most fields.

A pair "fits by name" when the thing f says it produces is the thing g says it
takes (deg -> deg, midi -> midi). Otherwise it only "fits by shape".

With thousands of functions there are millions of pairs, and (as the first
run showed) most pairs "work" merely because a number is a number. So each
function is tried against every slot that fits it BY NAME, plus a random
sample of the slots that fit only by shape.

Calls run in a child process with nothing in reach (sandbox.py); a call that
hangs is caught by a watchdog, the function is set aside, and the run restarts.

Run from the repository root:  python -I blender/blend.py --fresh
(with the Python that has numpy; --fresh is needed whenever the harvest changed)
Writes blender/_work/blend.json
"""
import json
import mmap
import os
import random
import re
import struct
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "_work")
HARVEST = os.path.join(WORK, "harvest.json")
PROBE = os.path.join(WORK, "probe.json")
OUT = os.path.join(WORK, "blend.json")
CULPRIT = os.path.join(WORK, "blend_culprit.txt")
EDGE_LOG = os.path.join(WORK, "blend_edges.jsonl")
NOW = os.path.join(WORK, "blend_now.bin")
SKIP = os.path.join(WORK, "blend_skip.json")
CALL_SECONDS = 1.0
## The parent kills the child if one call has not come back after this long (a loop the watchdog cannot interrupt).
STUCK_SECONDS = 6.0
## Slots that fit a function only by shape: how many to try, chosen at random.
SHAPE_SAMPLE = 60
## A function that has used this much time in all is set aside as too slow to blend.
SLOW_TOTAL = 4.0
WALKS_PER_SEED = 200
MAX_CHAIN = 16
KEEP_RECIPES = 60
SEEDS = ["f-round", "moth", "shipwreck", "Hello World 42", "C4", 440.0, 51.4778, 0.25, 7, 1987,
         [3, 1, 4, 1, 5, 9, 2, 6], [51.4778, -0.0015],
         [0.0, 0.38, 0.71, 0.92, 1.0, 0.92, 0.71, 0.38, 0.0, -0.38, -0.71, -0.92, -1.0, -0.92, -0.71, -0.38],
         [[2, 0, 1], [1, 3, 2], [1, 1, 4]], [[0, 0], [1, 2], [3, 1], [4, 4]]]

SYNONYMS = {
    "degree": "deg", "degrees": "deg", "angle": "deg", "radian": "rad", "radians": "rad",
    "frequency": "freq", "hz": "freq", "hertz": "freq", "f": "freq",
    "note": "midi", "pitch": "midi", "semitones": "midi", "semitone": "midi",
    "temperature": "temp", "kelvin": "temp", "celsius": "temp", "t": "temp",
    "latitude": "lat", "longitude": "lon", "lng": "lon",
    "colour": "color", "rgb": "color", "hex": "color",
    "string": "text", "str": "text", "s": "text", "word": "text", "msg": "text", "message": "text", "line": "text",
    "name": "text", "distance": "dist", "d": "dist", "metres": "dist", "meters": "dist", "m": "dist", "km": "dist",
    "seconds": "time", "sec": "time", "secs": "time", "ms": "time", "duration": "time",
    "bytes": "byte", "b": "byte", "val": "value", "v": "value", "x": "value", "n": "number", "num": "number",
    "arr": "list", "array": "list", "lst": "list", "values": "list", "data": "list", "seq": "list",
}


def norm(token):
    token = token.lower().strip("_")
    token = SYNONYMS.get(token, token)
    if token.endswith("s") and len(token) > 3:
        token = SYNONYMS.get(token[:-1], token[:-1])
    return token


def out_token(name):
    """What a function says it produces, going by its name."""
    low = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name).lower()
    m = re.search(r"_to_([a-z0-9_]+)$", low) or re.search(r"[a-z]2([a-z][a-z0-9_]*)$", low)
    if m:
        return norm(m.group(1).split("_")[-1] if "_" in m.group(1) and len(m.group(1)) > 14 else m.group(1))
    m = re.match(r"([a-z0-9]+)_from_", low)
    if m:
        return norm(m.group(1))
    m = re.match(r"(?:get|compute|calc|calculate|make|find|to)_([a-z0-9_]+)$", low)
    if m:
        return norm(m.group(1))
    return ""


def in_token(name, param):
    """What a function says it takes, going by its name and the argument's name."""
    low = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name).lower()
    m = re.match(r"([a-z0-9]+)_to_", low) or re.match(r"([a-z][a-z0-9]*)2[a-z]", low)
    tokens = {norm(param)}
    if m:
        tokens.add(norm(m.group(1)))
    m = re.search(r"_from_([a-z0-9_]+)$", low)
    if m:
        tokens.add(norm(m.group(1)))
    tokens.discard("")
    return tokens


GENERIC = {"value", "number", "list", "text", "result", "output", "data", "item"}


# ------------------------------------------------------------------ child

class Watch:
    """Kills the process if one call runs too long, leaving a note of which function it was."""

    def __init__(self):
        self.current = None
        self.since = 0.0
        self.spent = {}
        self.calls = 0
        # Which function is being called right now, where the parent can see it without us doing anything.
        self.file = open(NOW, "r+b")
        self.now = mmap.mmap(self.file.fileno(), 16)
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        while True:
            time.sleep(0.2)
            fid = self.current
            if fid is not None and time.time() - self.since > CALL_SECONDS:
                with open(CULPRIT, "w") as fh:
                    fh.write(str(fid))
                os._exit(3)

    def call(self, fid, fn, args):
        if self.spent.get(fid, 0.0) > SLOW_TOTAL:
            return False, None
        self.current, self.since = fid, time.time()
        self.calls += 1
        struct.pack_into("<qq", self.now, 0, fid, self.calls)
        try:
            return True, fn(*args)
        except BaseException as exc:  # noqa: BLE001
            if isinstance(exc, (KeyboardInterrupt, SystemExit)):
                raise
            return False, None
        finally:
            self.spent[fid] = self.spent.get(fid, 0.0) + (time.time() - self.since)
            self.current = None
            struct.pack_into("<q", self.now, 0, -1)


def child(skip):
    sys.path.insert(0, HERE)
    import sandbox
    sys.setrecursionlimit(400)
    functions = {f["id"]: f for f in json.load(open(HARVEST, encoding="utf-8"))["functions"]}
    records = json.load(open(PROBE, encoding="utf-8"))["records"]
    watch = Watch()
    bridge = sandbox.NodeBridge()

    live = {}     # fid -> callable
    slots = {}    # fid -> [{"pos", "kind", "fixed": [...], "out"}]
    for rec in records:
        fid = rec["id"]
        if not rec["sigs"] or fid in skip:
            continue
        try:
            live[fid] = sandbox.load(functions[fid], bridge)
        except Exception:  # noqa: BLE001
            continue
        mine, seen = [], set()
        for sig in rec["sigs"]:
            fixed = json.loads(sig["examples"][0][0])
            for pos, k in enumerate(sig["in"]):
                if (pos, k) in seen:
                    continue
                seen.add((pos, k))
                mine.append({"pos": pos, "kind": k, "fixed": fixed, "out": sig["out"],
                             "wanted": in_token(functions[fid]["name"], functions[fid]["params"][pos])})
        slots[fid] = mine

    def run(fid, slot, value):
        """Call a function with `value` in the slot's position and its other arguments as probed."""
        args = json.loads(json.dumps(slot["fixed"]))
        args[slot["pos"]] = json.loads(json.dumps(value))
        ok, result = watch.call(fid, live[fid], args)
        if not ok or result is None or not sandbox.tame(result):
            return False, None
        if isinstance(result, int) and not isinstance(result, bool) and abs(result) > 10 ** 7:
            return False, None
        if isinstance(result, float) and abs(result) > 1e12:
            return False, None
        k = sandbox.kind(result)
        if k not in sandbox.FITS:
            return False, None
        try:
            return True, json.loads(json.dumps(result))
        except (TypeError, ValueError):
            return False, None

    # What each function really gives back on its own probed inputs.
    gives = {}
    for rec in records:
        fid = rec["id"]
        if fid not in live:
            continue
        outs = []
        for sig in rec["sigs"][:2]:
            for example in sig["examples"]:
                ok, value = run(fid, {"pos": 0, "fixed": json.loads(example[0]), "kind": sig["in"][0], "out": sig["out"]},
                                json.loads(example[0])[0])
                if ok and value not in outs:
                    outs.append(value)
        if len(outs) >= 2:
            gives[fid] = outs[:4]

    # ---- pairs (written out per function, so a restart picks up where it stopped)
    attempted = worked = 0
    edges = []
    done = set()
    if os.path.exists(EDGE_LOG):
        for line in open(EDGE_LOG, encoding="utf-8"):
            if line.strip():
                entry = json.loads(line)
                done.add(entry["f"])
                attempted += entry["attempted"]
                edges.extend(e for e in entry["edges"] if e["g"] not in skip and e["f"] not in skip)
    edge_log = open(EDGE_LOG, "a", encoding="utf-8")
    for f, outs in gives.items():
        if f in done:
            continue
        mine, tried = [], 0
        kinds = {sandbox.kind(v) for v in outs}
        if len(kinds) != 1:
            edge_log.write(json.dumps({"f": f, "attempted": 0, "edges": []}) + chr(10))
            continue
        out_kind = kinds.pop()
        produced = out_token(functions[f]["name"])
        by_name, by_shape = [], []
        for g, g_slots in slots.items():
            if g == f or functions[g]["repo"] == functions[f]["repo"]:
                continue
            for slot in g_slots:
                if slot["kind"] not in sandbox.FITS.get(out_kind, ()):
                    continue
                if produced and produced not in GENERIC and produced in slot["wanted"]:
                    by_name.append((g, slot))
                else:
                    by_shape.append((g, slot))
        picker = random.Random(f)
        if len(by_shape) > SHAPE_SAMPLE:
            by_shape = picker.sample(by_shape, SHAPE_SAMPLE)
        if len(by_name) > 4 * SHAPE_SAMPLE:
            by_name = picker.sample(by_name, 4 * SHAPE_SAMPLE)
        for g, slot in by_name + by_shape:
            if True:
                attempted += 1
                tried += 1
                results = []
                for value in outs:
                    ok, result = run(g, slot, value)
                    if ok:
                        results.append(json.dumps(result))
                if len(results) < 2 or len(set(results)) < 2:
                    continue
                if all(r == json.dumps(v) for r, v in zip(results, outs)):
                    continue  # g handed back what it was given
                named = bool(produced) and produced in slot["wanted"] and produced not in GENERIC
                mine.append({"f": f, "g": g, "pos": slot["pos"], "kind": slot["kind"], "fixed": slot["fixed"],
                             "named": named, "token": produced if named else ""})
        edges.extend(mine)
        edge_log.write(json.dumps({"f": f, "attempted": tried, "edges": mine}) + chr(10))
        edge_log.flush()
    edge_log.close()
    worked = len(edges)

    by_from = {}
    for e in edges:
        by_from.setdefault(e["f"], []).append(e)

    # Wrappers: functions that only put what they were given inside a labelled box ({"type": ..., "value": x}).
    # They accept anything and change nothing, so chains would run through them forever. They stay in the
    # blend, but a chain is made to prefer almost anything else.
    def flat(text):
        return re.sub(r"\.0(?![0-9])", "", text)

    wrappers = set()
    for rec in records:
        hits = total = 0
        for sig in rec["sigs"]:
            if sig["out"] != "dict":
                continue
            for example in sig["examples"]:
                total += 1
                if flat(json.dumps(json.loads(example[0])[0])) in flat(example[1]):
                    hits += 1
        if total and hits == total:
            wrappers.add(rec["id"])

    def weigh(e, here, repos, shelves):
        g = functions[e["g"]]
        return ((6.0 if e["named"] else 1.0) * (3.0 if g["shelf"] not in shelves else 1.0)
                * (2.0 if g["repo"] not in repos else 0.5) * (2.0 if g["lang"] != here else 1.0)
                * (3.0 if g.get("numpy") else 1.0) * (0.03 if e["g"] in wrappers else 1.0))

    # ---- chains
    rng = random.Random(20261123)
    recipes = []
    starters = {}
    for fid, g_slots in slots.items():
        for slot in g_slots:
            if slot["pos"] == 0:
                starters.setdefault(slot["kind"], []).append((fid, slot))
    for seed in SEEDS:
        seed_kind = sandbox.kind(seed)
        pool = [s for k in sandbox.FITS.get(seed_kind, ()) for s in starters.get(k, [])]
        for walk in range(WALKS_PER_SEED):
            if not pool:
                break
            fid, slot = rng.choice(pool)
            ok, value = run(fid, slot, seed)
            if not ok:
                continue
            steps = [{"f": fid, "pos": slot["pos"], "fixed": slot["fixed"], "named": False, "value": value}]
            used, repos, shelves = {fid}, {functions[fid]["repo"]}, {functions[fid]["shelf"]}
            while len(steps) < MAX_CHAIN:
                options = [e for e in by_from.get(steps[-1]["f"], []) if e["g"] not in used]
                if not options:
                    break
                if len(options) > 48:
                    # Plenty to choose from: always consider the links by name, and a sample of the rest.
                    options = [e for e in options if e["named"]][:16] + rng.sample(options, 32)
                here = functions[steps[-1]["f"]]["lang"]
                weights = [weigh(e, here, repos, shelves) for e in options]
                moved = False
                for attempt in range(8):
                    e = rng.choices(options, weights)[0]
                    ok, result = run(e["g"], e, steps[-1]["value"])
                    if ok and result != steps[-1]["value"]:
                        steps.append({"f": e["g"], "pos": e["pos"], "fixed": e["fixed"], "named": e["named"], "value": result})
                        used.add(e["g"])
                        repos.add(functions[e["g"]]["repo"])
                        shelves.add(functions[e["g"]]["shelf"])
                        moved = True
                        break
                if not moved:
                    break
            if len(steps) >= 4:
                langs = [("js" if functions[s["f"]]["lang"] == "js" else "np" if functions[s["f"]].get("numpy") else "py") for s in steps]
                recipes.append({"seed": seed, "steps": steps, "repos": len(repos), "shelves": len(shelves),
                                "named": sum(1 for s in steps if s["named"]), "numpy": langs.count("np"),
                                "javascript": langs.count("js"), "wrappers": sum(1 for s in steps if s["f"] in wrappers)})
    recipes.sort(key=lambda r: (r["shelves"] + 2 * r["named"] + r["numpy"] + min(r["javascript"], 4) - 3 * r["wrappers"],
                                len(r["steps"])), reverse=True)
    kept, seen_sets = [], []
    for r in recipes:
        ids = frozenset(s["f"] for s in r["steps"])
        if any(len(ids & other) > 0.6 * len(ids) for other in seen_sets):
            continue
        seen_sets.append(ids)
        kept.append(r)
        if len(kept) >= KEEP_RECIPES:
            break

    in_edges = {e["f"] for e in edges} | {e["g"] for e in edges}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({
            "stats": {"functions_live": len(live), "pairs_attempted": attempted, "pairs_worked": worked,
                      "named_pairs": sum(1 for e in edges if e["named"]),
                      "functions_connected": len(in_edges),
                      "repos_connected": len({functions[i]["repo"] for i in in_edges}),
                      "shelves_connected": len({functions[i]["shelf"] for i in in_edges}),
                      "walks": len(recipes), "skipped_for_hanging": sorted(skip), "wrappers": sorted(wrappers),
                      "set_aside_as_slow": sorted(i for i, t in watch.spent.items() if t > SLOW_TOTAL)},
            "edges": edges, "recipes": kept,
        }, fh, ensure_ascii=False)


# ----------------------------------------------------------------- parent

def parent():
    skip = []
    if "--fresh" in sys.argv:
        for old in (EDGE_LOG, SKIP):
            if os.path.exists(old):
                os.remove(old)
    if os.path.exists(SKIP):
        skip = json.load(open(SKIP))   # functions an earlier run of the same harvest set aside for hanging
    errors = os.path.join(WORK, "blend_errors.txt")
    for attempt in range(200):
        if os.path.exists(CULPRIT):
            os.remove(CULPRIT)
        with open(NOW, "wb") as fh:
            fh.write(struct.pack("<qq", -1, 0))
        with open(errors, "wb") as err:
            proc = subprocess.Popen([sys.executable, "-I", os.path.abspath(__file__), "--child", json.dumps(skip)],
                                    stdout=subprocess.DEVNULL, stderr=err)
            last, since, stuck = None, time.time(), None
            while proc.poll() is None:
                time.sleep(0.5)
                with open(NOW, "rb") as fh:
                    now = struct.unpack("<qq", fh.read(16))
                if now != last:
                    last, since = now, time.time()
                elif now[0] >= 0 and time.time() - since > STUCK_SECONDS:
                    stuck = now[0]
                    proc.kill()
                    proc.wait()
                    break
        if stuck is None and proc.returncode != 0 and os.path.exists(CULPRIT):
            stuck = int(open(CULPRIT).read().strip())
        if stuck is not None:
            skip.append(stuck)
            json.dump(skip, open(SKIP, "w"))
            continue
        if proc.returncode == 0:
            break
        print("child failed:", open(errors, encoding="utf-8", errors="replace").read()[-600:])
        sys.exit(1)
    data = json.load(open(OUT, encoding="utf-8"))
    s = data["stats"]
    print(f"{s['functions_live']} functions live; {s['pairs_attempted']} cross-repository pairs tried, "
          f"{s['pairs_worked']} really work ({100.0 * s['pairs_worked'] / max(1, s['pairs_attempted']):.1f}%), "
          f"{s['named_pairs']} of those fit by name")
    print(f"connected: {s['functions_connected']} functions from {s['repos_connected']} repositories on {s['shelves_connected']} shelves; "
          f"{len(data['recipes'])} chains kept of {s['walks']} found; set aside for hanging: {s['skipped_for_hanging']}, as slow: {s['set_aside_as_slow']}")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--child":
        child(set(json.loads(sys.argv[2])))
    else:
        parent()
