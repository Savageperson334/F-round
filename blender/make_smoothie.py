"""Pour the blend: write out the fused program and its paperwork.

From blender/_work/ (harvest, probe, blend) this writes, into blender/:

  berries/bNNNN_<name>.py   one file per real function that connected to at
  berries/bNNNN_<name>.js   least one function from another repository. The
                            function's source is copied VERBATIM, under a
                            header saying exactly where it came from.
  blend_map.json            which function feeds which, and the long chains found
  CONNECTIONS.md            what connected, in words and numbers
  CREDITS.md                every repository whose code is in the blend
  licenses/                 each of those repositories' own licence file
  COPYING                   the GNU GPL v3, under which the blend as a whole is released

Run from the repository root:  python -I blender/make_smoothie.py
"""
import json
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "_work")
BERRIES_SRC = os.path.join(HERE, "_berries")
BERRIES_OUT = os.path.join(HERE, "berries")
LICENSES_OUT = os.path.join(HERE, "licenses")
LICENCE_NAMES = ("license", "licence", "copying", "unlicense", "notice")


def slug(text):
    return re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")[:40]


def licence_file(repo):
    folder = os.path.join(BERRIES_SRC, repo.replace("/", "__"))
    found = []
    if os.path.isdir(folder):
        for name in sorted(os.listdir(folder)):
            if name.lower().split(".")[0] in LICENCE_NAMES and os.path.isfile(os.path.join(folder, name)):
                found.append(os.path.join(folder, name))
    return found


def main():
    functions = {f["id"]: f for f in json.load(open(os.path.join(WORK, "harvest.json"), encoding="utf-8"))["functions"]}
    probe = {r["id"]: r for r in json.load(open(os.path.join(WORK, "probe.json"), encoding="utf-8"))["records"]}
    blend = json.load(open(os.path.join(WORK, "blend.json"), encoding="utf-8"))
    edges = blend["edges"]
    wrappers = set(blend["stats"].get("wrappers", []))
    used = sorted({e["f"] for e in edges} | {e["g"] for e in edges})

    # ---- the berries
    if os.path.isdir(BERRIES_OUT):
        shutil.rmtree(BERRIES_OUT)
    os.makedirs(BERRIES_OUT)
    open(os.path.join(BERRIES_OUT, "__init__.py"), "w", encoding="utf-8").write(
        '"""Real functions copied verbatim from other people\'s repositories. See each file\'s header and ../CREDITS.md."""\n')
    modules = {}
    for fid in used:
        f = functions[fid]
        js = f["lang"] == "js"
        mark = "//" if js else "#"
        module = "b%04d_%s" % (fid, slug(f["name"]))
        modules[fid] = module
        if f["file"].endswith(".ipynb.py"):
            where = "notebook %s (its code cells joined in order; line %d of those)" % (f["file"][:-3], f["line"])
        else:
            where = "file %s, line %d" % (f["file"], f["line"])
        lines = [
            "%s" % f["name"],
            "",
            "Copied verbatim from %s" % f["url"],
            "  " + where,
            "  licence (as GitHub reports it): %s   see ../licenses/" % f["licence"],
            "  catalogue shelf: %s" % f["shelf"],
        ]
        if f["also_in"]:
            lines.append("  the same function also appears in: %s" % ", ".join(f["also_in"]))
        lines += [
            "",
            "Everything below the line is that repository's code, unmodified. Imports, constants and",
            "helper functions it needs from the same file are included, also unmodified.",
            "-" * 76,
        ]
        lines = [(mark + " " + line).rstrip() for line in lines] + [""]
        lines += f["imports"]
        if f["imports"]:
            lines.append("")
        for const in f["consts"]:
            lines += [const["source"], ""]
        for helper in f["helpers"]:
            lines += ["", helper["source"], ""]
        lines += ["", f["source"], ""]
        with open(os.path.join(BERRIES_OUT, module + (".js" if js else ".py")), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lines))

    # ---- the map
    # The other arguments each function is called with are kept once per function and referred to by number.
    fixed_sets = {fid: [] for fid in used}

    def fixed_index(fid, fixed):
        sets = fixed_sets[fid]
        if fixed not in sets:
            sets.append(fixed)
        return sets.index(fixed)

    by_from = {}
    for e in edges:
        by_from.setdefault(str(e["f"]), []).append([e["g"], e["pos"], fixed_index(e["g"], e["fixed"]), 1 if e["named"] else 0, e["token"]])
    info = {}
    for fid in used:
        f = functions[fid]
        starts, seen = [], set()
        for sig in probe[fid]["sigs"]:
            k = sig["in"][0]
            if k not in seen:
                seen.add(k)
                starts.append({"kind": k, "fixed": fixed_index(fid, json.loads(sig["examples"][0][0]))})
        info[str(fid)] = {"module": modules[fid], "lang": f["lang"], "numpy": bool(f.get("numpy")),
                          "wrapper": fid in wrappers, "name": f["name"],
                          "repo": f["repo"], "url": f["url"], "file": f["file"],
                          "line": f["line"], "licence": f["licence"], "shelf": f["shelf"], "doc": f["doc"],
                          "params": f["params"], "starts": starts, "fixed": fixed_sets[fid]}
    recipes = [{"seed": r["seed"], "steps": [[s["f"], s["pos"], s["fixed"], s["named"]] for s in r["steps"]],
                "repos": r["repos"], "shelves": r["shelves"], "named": r["named"], "numpy": r.get("numpy", 0),
                "javascript": r.get("javascript", 0)} for r in blend["recipes"]]
    with open(os.path.join(HERE, "blend_map.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"stats": blend["stats"], "functions": info, "edges": by_from, "recipes": recipes}, fh, ensure_ascii=False)

    # ---- licences
    if os.path.isdir(LICENSES_OUT):
        shutil.rmtree(LICENSES_OUT)
    os.makedirs(LICENSES_OUT)
    repos = {}
    for fid in used:
        f = functions[fid]
        repos.setdefault(f["repo"], {"url": f["url"], "licence": f["licence"], "shelf": f["shelf"], "functions": []})
        repos[f["repo"]]["functions"].append(f)
    gpl_text = None
    missing = []
    for repo, r in sorted(repos.items()):
        files = licence_file(repo)
        if not files:
            missing.append(repo)
            r["licence_file"] = ""
            continue
        target = repo.replace("/", "__") + ".txt"
        with open(os.path.join(LICENSES_OUT, target), "w", encoding="utf-8", newline="\n") as out:
            for path in files:
                text = open(path, encoding="utf-8", errors="replace").read()
                out.write("===== %s : %s =====\n\n%s\n\n" % (repo, os.path.basename(path), text))
                if gpl_text is None and r["licence"] == "GPL-3.0" and "GNU GENERAL PUBLIC LICENSE" in text[:400] and "Version 3" in text[:400]:
                    gpl_text = text
        r["licence_file"] = "licenses/" + target
    if gpl_text:
        open(os.path.join(HERE, "COPYING"), "w", encoding="utf-8", newline="\n").write(gpl_text)

    # ---- credits
    out = ["# Credits", "",
           "Every repository whose code is in the blend. Each function listed was copied verbatim into `berries/`, "
           "with its origin in the file header. The blend as a whole is released under the GNU GPL v3 or later (`COPYING`); "
           "each piece remains under its own licence, kept in `licenses/`.", "",
           "Licences are as GitHub reports them for each repository on 2026-11-22. "
           + ("%d repositories have no licence file at their top level; their licence is recorded from GitHub's metadata only: %s." % (len(missing), ", ".join(missing)) if missing else "Every repository's own licence file is included."),
           "", "| Repository | Licence | Shelf | Functions used |", "| --- | --- | --- | --- |"]
    for repo, r in sorted(repos.items(), key=lambda kv: kv[0].lower()):
        names = ", ".join("`%s` (%s:%d)" % (f["name"], f["file"], f["line"]) for f in sorted(r["functions"], key=lambda f: f["name"]))
        licence = "[%s](%s)" % (r["licence"], r["licence_file"]) if r["licence_file"] else r["licence"]
        out.append("| [%s](%s) | %s | %s | %s |" % (repo, r["url"], licence, r["shelf"], names))
    open(os.path.join(HERE, "CREDITS.md"), "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")

    # ---- connections
    s = blend["stats"]
    shelf_pairs = {}
    for e in edges:
        a, b = functions[e["f"]]["shelf"], functions[e["g"]]["shelf"]
        if a != b:
            shelf_pairs[tuple(sorted((a, b)))] = shelf_pairs.get(tuple(sorted((a, b))), 0) + 1
    named = [e for e in edges if e["named"]]
    con = ["# What connected", "",
           "Generated by `make_smoothie.py` from a real run. Nothing here is hand-picked.", "",
           "- **%d** functions were harvested and **%d** of them ran on something when tried." % (len(functions), sum(1 for r in probe.values() if r["sigs"])),
           "- In the blend: **%d** Python functions (**%d** of them numpy code, **%d** from notebooks) and **%d** JavaScript functions." % (
               sum(1 for i in used if functions[i]["lang"] == "py"), sum(1 for i in used if functions[i].get("numpy")),
               sum(1 for i in used if functions[i]["file"].endswith(".ipynb.py")), sum(1 for i in used if functions[i]["lang"] == "js")),
           "- **%d** pairs of functions from different repositories were tried by feeding one's real output to the other "
           "(every pair that fits by name, and a random sample of those that fit only by shape)." % s["pairs_attempted"],
           "- **%d** pairs really work (%.1f%%). The rest raised an error, returned nothing, or ignored what they were given." % (s["pairs_worked"], 100.0 * s["pairs_worked"] / max(1, s["pairs_attempted"])),
           "- **%d** of the working pairs fit by name: what the first says it produces is what the second says it takes. The others fit only by shape (a number is a number)." % s["named_pairs"],
           "- The connected functions come from **%d** repositories on **%d** shelves, and join **%d** different pairs of shelves." % (s["repos_connected"], s["shelves_connected"], len(shelf_pairs)),
           "", "## Pairs that fit by name", "",
           "These are the ones that can be meaningful: two strangers' functions that agree, by their names, on what the value is. "
           "Some are genuine and many are loose; the matching is a short word list, not understanding.", "",
           "| Produces | From | Feeds | In | Shared word |", "| --- | --- | --- | --- | --- |"]
    seen_pairs = set()
    for e in sorted(named, key=lambda e: (e["token"], functions[e["f"]]["repo"])):
        f, g = functions[e["f"]], functions[e["g"]]
        key = (f["id"], g["id"])
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        con.append("| `%s` | [%s](%s) | `%s` | [%s](%s) | %s |" % (f["name"], f["repo"], f["url"], g["name"], g["repo"], g["url"], e["token"]))
        if len(seen_pairs) >= 120:
            con.append("| ... | | | | %d more |" % (len(named) - 120))
            break
    con += ["", "## The longest chains found", "",
            "Each line is a real call. The value on the right is what that function returned and what the next one was given.", ""]
    for i, r in enumerate(blend["recipes"][:8]):
        con.append("### Chain %d: seed `%s`, %d steps, %d repositories, %d shelves, %d links by name" % (
            i, json.dumps(r["seed"]), len(r["steps"]), r["repos"], r["shelves"], r["named"]))
        con.append("")
        con.append("| Function | Repository | Shelf | Returned |")
        con.append("| --- | --- | --- | --- |")
        for st in r["steps"]:
            f = functions[st["f"]]
            value = json.dumps(st["value"], ensure_ascii=False)
            tongue = "JavaScript" if f["lang"] == "js" else ("numpy" if f.get("numpy") else "Python")
            con.append("| `%s` (%s)%s | [%s](%s) | %s | `%s` |" % (f["name"], tongue, ", by name" if st["named"] else "", f["repo"], f["url"], f["shelf"],
                                                      (value[:70] + "...") if len(value) > 70 else value.replace("|", "\\|")))
        con.append("")
    con += ["## Shelves that met most often", "", "| Shelf | Shelf | Working pairs |", "| --- | --- | --- |"]
    for (a, b), n in sorted(shelf_pairs.items(), key=lambda kv: -kv[1])[:25]:
        con.append("| %s | %s | %d |" % (a, b, n))
    open(os.path.join(HERE, "CONNECTIONS.md"), "w", encoding="utf-8", newline="\n").write("\n".join(con) + "\n")

    print("%d berries written from %d repositories; %d licence files; %d repositories without one; %d shelf pairs" % (
        len(used), len(repos), len(repos) - len(missing), len(missing), len(shelf_pairs)))
    print({"python": sum(1 for i in used if functions[i]["lang"] == "py"), "numpy": sum(1 for i in used if functions[i].get("numpy")),
           "notebook": sum(1 for i in used if functions[i]["file"].endswith(".ipynb.py")),
           "javascript": sum(1 for i in used if functions[i]["lang"] == "js"),
           "map MB": round(os.path.getsize(os.path.join(HERE, "blend_map.json")) / 1e6, 1)})


if __name__ == "__main__":
    main()
