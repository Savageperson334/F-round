"""Find out what each harvested function actually accepts, by trying it.

For every function in blender/_work/harvest.json this calls it with batteries
of plain sample values (numbers, text, lists) and records which shapes of
argument it runs on, what shape it returns, and a few real examples.

Most attempts fail, which is the point: what is left is what really works.

Calls happen in a child process with nothing in reach (see sandbox.py). The
parent watches it: a function that hangs or crashes the child is recorded as
such and skipped, and the child is restarted after it.

Run from the repository root:  python -I blender/probe.py
(with the Python that has numpy, if numpy functions are to be tried)
Writes blender/_work/probe.json
"""
import itertools
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "_work")
HARVEST = os.path.join(WORK, "harvest.json")
LOG = os.path.join(WORK, "probe.jsonl")
OUT = os.path.join(WORK, "probe.json")
STALL_SECONDS = 6.0
## Time one function may use in all before we stop trying new kinds of argument on it.
FUNCTION_SECONDS = 2.5

SAMPLES = {
    "int": [0, 1, 7, 60, 440, 1987],
    "float": [0.25, 2.0, 37.2, 440.0, 51.4778],
    "str": ["f-round", "Hello World 42", "abc", "C4", "The quick brown fox"],
    "nums": [[3, 1, 4, 1, 5, 9, 2, 6], [0.1, 0.5, 0.9, 0.3],
             [0.0, 0.38, 0.71, 0.92, 1.0, 0.92, 0.71, 0.38, 0.0, -0.38, -0.71, -0.92, -1.0, -0.92, -0.71, -0.38],
             [1.0, 2.0, 2.0], [440.0, 880.0, 660.0], [51.4778, -0.0015]],
    "strs": [["cave", "orbit", "moth"], ["a", "b", "c", "d"], ["C4", "E4", "G4"]],
    "table": [[[1, 0], [0, 1]], [[0.1, 0.2], [0.3, 0.4], [0.5, 0.9]], [[2, 0, 1], [1, 3, 2], [1, 1, 4]],
              [[0, 0], [1, 2], [3, 1], [4, 4]], [[3, 4, 5], [6, 8, 10]]],
    "bool": [True, False],
    "dict": [{"a": 1, "b": 2}, {"x": 0.5, "y": 0.25}],
}
KINDS = ["int", "float", "str", "nums", "strs", "table"]

# A parameter's name is a hint about what to try first. It is only a hint: the call decides.
HINTS = [
    (("text", "string", "str", "word", "name", "msg", "message", "line", "char", "note", "key", "code", "label", "s"), ["str"]),
    (("list", "array", "arr", "values", "vals", "seq", "data", "samples", "points", "coords", "vec", "vector", "xs", "ys", "rgb", "hsv", "color", "colour", "lst", "items"), ["nums", "table", "strs"]),
    (("n", "num", "count", "size", "length", "len", "index", "idx", "i", "k", "midi", "octave", "steps", "order", "bits", "year", "month", "day"), ["int", "float"]),
    (("matrix", "mat", "grid", "table", "rows"), ["table"]),
]


def hinted(param, arrays):
    low = param.lower()
    for names, kinds in HINTS:
        if low in names or any(low.endswith("_" + n) or low.startswith(n + "_") for n in names if len(n) > 2):
            return kinds
    return ["nums", "float", "table"] if arrays else ["float", "int"]


def kind_combos(params, arrays=False):
    """Kind combinations worth trying for these parameters, likeliest first, capped."""
    k = len(params)
    seen, out = set(), []

    def add(combo):
        if combo not in seen:
            seen.add(combo)
            out.append(combo)

    hints = [hinted(p, arrays) for p in params]
    for combo in itertools.islice(itertools.product(*hints), 12):
        add(combo)
    for one in KINDS:
        add(tuple([one] * k))
    if k == 1:
        for one in ("bool", "dict"):
            add((one,))
    if k == 2:
        for a, b in itertools.product(KINDS, KINDS):
            add((a, b))
    if k == 3:
        for a, b, c in itertools.product(("int", "float", "str", "nums"), repeat=3):
            add((a, b, c))
    return out[:70]


# ------------------------------------------------------------------ child

def child(start):
    sys.path.insert(0, HERE)
    import sandbox
    sys.setrecursionlimit(400)
    functions = json.load(open(HARVEST, encoding="utf-8"))["functions"]
    bridge = sandbox.NodeBridge()
    with open(LOG, "a", encoding="utf-8") as log:
        for function in functions:
            if function["id"] < start:
                continue
            log.write(json.dumps({"begin": function["id"]}) + "\n")
            log.flush()
            record = {"id": function["id"], "sigs": []}
            try:
                fn = sandbox.load(function, bridge)
            except Exception as exc:  # noqa: BLE001
                record["status"] = "will not load: " + type(exc).__name__
                log.write(json.dumps(record) + "\n")
                log.flush()
                continue
            params = function["params"][: function["required"]]
            began = time.time()
            for combo in kind_combos(params, bool(function.get("numpy"))):
                if time.time() - began > FUNCTION_SECONDS:
                    record["slow"] = True
                    break
                results = []
                for pick in range(4):
                    if time.time() - began > FUNCTION_SECONDS:
                        break
                    args = [SAMPLES[k][(pick + i) % len(SAMPLES[k])] for i, k in enumerate(combo)]
                    frozen = json.dumps(args)
                    try:
                        value = fn(*json.loads(frozen))
                    except BaseException as exc:  # noqa: BLE001
                        if isinstance(exc, (KeyboardInterrupt, SystemExit)):
                            raise
                        continue
                    if value is None or not sandbox.tame(value):
                        continue
                    out_kind = sandbox.kind(value)
                    if out_kind in ("other", "none", "empty", "seq"):
                        continue
                    try:
                        again = fn(*json.loads(frozen))
                    except BaseException:  # noqa: BLE001
                        continue
                    if again != value:
                        continue  # not deterministic
                    results.append((frozen, out_kind, json.dumps(value)))
                if len(results) < 2:
                    continue
                if len({r[2] for r in results}) < 2:
                    continue  # the answer does not depend on the input
                kinds_out = {r[1] for r in results}
                if len(kinds_out) != 1:
                    continue
                record["sigs"].append({"in": list(combo), "out": results[0][1], "ok": len(results),
                                       "examples": [[r[0], r[2][:300]] for r in results[:3]]})
            record["status"] = "ok" if record["sigs"] else ("too slow" if record.get("slow") else "runs on nothing we tried")
            log.write(json.dumps(record) + "\n")
            log.flush()
        log.write(json.dumps({"finished": True}) + "\n")


# ----------------------------------------------------------------- parent

def parent():
    functions = json.load(open(HARVEST, encoding="utf-8"))["functions"]
    if os.path.exists(LOG):
        os.remove(LOG)
    open(LOG, "w").close()
    start, restarts, hung = 0, 0, []
    while True:
        proc = subprocess.Popen([sys.executable, "-I", os.path.abspath(__file__), "--child", str(start)],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        last_size, last_change = -1, time.time()
        while proc.poll() is None:
            time.sleep(0.25)
            size = os.path.getsize(LOG)
            if size != last_size:
                last_size, last_change = size, time.time()
            elif time.time() - last_change > STALL_SECONDS:
                proc.kill()
                break
        proc.wait()
        lines = [json.loads(l) for l in open(LOG, encoding="utf-8") if l.strip()]
        if lines and lines[-1].get("finished"):
            break
        # The child died or hung in the function it last began.
        begun = [l["begin"] for l in lines if "begin" in l]
        done = {l["id"] for l in lines if "id" in l}
        stuck = begun[-1] if begun else start
        if stuck not in done:
            hung.append(stuck)
            with open(LOG, "a", encoding="utf-8") as log:
                log.write(json.dumps({"id": stuck, "sigs": [], "status": "hung or crashed"}) + "\n")
        start = stuck + 1
        restarts += 1
        if start >= len(functions) or restarts > 400:
            break
    records = {}
    for line in open(LOG, encoding="utf-8"):
        if line.strip():
            entry = json.loads(line)
            if "id" in entry:
                records[entry["id"]] = entry
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"records": [records[i] for i in sorted(records)]}, fh, ensure_ascii=False)
    usable = sum(1 for r in records.values() if r["sigs"])
    print(f"{len(records)} functions tried: {usable} run on something, "
          f"{sum(1 for r in records.values() if r['status'] == 'runs on nothing we tried')} run on nothing we tried, "
          f"{sum(1 for r in records.values() if r['status'].startswith('will not load'))} would not load, "
          f"{len(hung)} hung or crashed ({restarts} restarts)")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--child":
        child(int(sys.argv[2]))
    else:
        parent()
