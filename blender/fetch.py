"""Fetch the source of catalogue repositories whose licence allows copying.

Berries for the blender. For each selected repository this downloads the
default-branch zip from GitHub and keeps ONLY, in blender/_berries/<owner>__<repo>/:

  - its .py files
  - the code cells of its notebooks, joined in order into <name>.ipynb.py
  - its .js / .mjs / .cjs files (not minified or vendored ones)
  - its licence files

Nothing downloaded is ever run, imported or installed: it is read as text by
harvest.py and harvest_js.js.

Selection (from data/F_ROUND_MASTER_4100.csv):
  - licence one of ALLOWED (permissive, plus GPL-3 / LGPL: the blend itself is
    released under GPL-3.0-or-later, which all of these can be combined into;
    GPL-2.0 and AGPL-3.0 are left out because they may not be)
  - not a fork
  - at most MAX_KB, whatever its main language (Python turns up everywhere), or
    at most MAX_KB_CODE when its main language is one we can harvest

Run from the repository root:  python -I blender/fetch.py [limit]
Needs the GitHub CLI (gh), logged in. Safe to re-run: fetched repos are skipped.
"""
import ast
import concurrent.futures
import csv
import io
import json
import os
import subprocess
import sys
import warnings
import zipfile

warnings.simplefilter("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "data", "F_ROUND_MASTER_4100.csv")
BERRIES = os.path.join(ROOT, "blender", "_berries")
ALLOWED = {"MIT", "Apache-2.0", "BSD-3-Clause", "BSD-2-Clause", "Unlicense", "CC0-1.0", "ISC", "0BSD", "Zlib",
           "MPL-2.0", "BSL-1.0", "GPL-3.0", "LGPL-3.0", "LGPL-2.1"}
CODE_LANGUAGES = {"Python", "Jupyter Notebook", "JavaScript"}
MAX_KB = 15000
MAX_KB_CODE = 60000
MAX_PY_BYTES = 400_000
MAX_JS_BYTES = 300_000
MAX_NOTEBOOK_BYTES = 8_000_000
MAX_LICENCE_BYTES = 120_000
LICENCE_NAMES = ("license", "licence", "copying", "notice", "unlicense")
SKIP_PARTS = {"node_modules", "site-packages", "venv", ".venv", "bower_components", "vendor", "vendors",
              "third_party", "thirdparty", "dist", "build", "__pycache__", ".git"}
## Bump when what is kept changes, so that already-fetched repositories are fetched again.
KEEPS = 2


def selected():
    with open(MASTER, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        if r["License (verify)"] not in ALLOWED or r["Fork?"] == "true":
            continue
        size = int(r["Repository size KB"] or 0)
        if size > (MAX_KB_CODE if r["Primary language"] in CODE_LANGUAGES else MAX_KB):
            continue
        out.append(r)
    return out


def folder(repo):
    return os.path.join(BERRIES, repo.replace("/", "__"))


def notebook_code(raw):
    """The code cells of a notebook, joined in order, as text. Returns "" if there is nothing usable.

    Lines that are notebook commands (%magic, !shell) are not Python; each is replaced by a call to
    a name no harvested function may use, so that a function containing one is never kept. A cell
    that is not valid Python on its own is left out.
    """
    try:
        book = json.loads(raw.decode("utf-8", "replace"))
        cells = book.get("cells")
        if cells is None:
            cells = [c for sheet in book.get("worksheets", []) for c in sheet.get("cells", [])]
    except Exception:  # noqa: BLE001
        return ""
    parts = []
    for number, cell in enumerate(cells):
        if not isinstance(cell, dict) or cell.get("cell_type") != "code":
            continue
        source = cell.get("source", cell.get("input", ""))
        if isinstance(source, list):
            source = "".join(str(s) for s in source)
        if not isinstance(source, str) or not source.strip() or len(source) > 200_000:
            continue
        lines = []
        for line in source.split("\n"):
            bare = line.lstrip()
            if bare.startswith(("%", "!", "?")) or bare.rstrip().endswith("?"):
                line = line[: len(line) - len(bare)] + "__notebook_command__()"
            lines.append(line)
        text = "\n".join(lines)
        try:
            ast.parse(text)
        except BaseException as exc:  # noqa: BLE001
            if isinstance(exc, (KeyboardInterrupt, SystemExit)):
                raise
            continue
        parts.append("# ---- notebook code cell %d\n%s\n" % (number, text))
    return "\n\n".join(parts)


def fetch(row):
    repo = row["Repo"]
    dest = folder(repo)
    meta_path = os.path.join(dest, "_berry.json")
    if os.path.exists(meta_path):
        try:
            if json.load(open(meta_path, encoding="utf-8")).get("keeps", 1) >= KEEPS:
                return repo, "have", 0
        except Exception:  # noqa: BLE001
            pass
    try:
        got = subprocess.run(["gh", "api", f"repos/{repo}/zipball"], capture_output=True, timeout=420)
    except Exception as exc:  # noqa: BLE001
        return repo, f"failed: {type(exc).__name__}", 0
    if got.returncode != 0 or not got.stdout.startswith(b"PK"):
        return repo, "failed: " + got.stderr.decode("utf-8", "replace")[:120].strip(), 0
    kept = {"py": 0, "notebook": 0, "js": 0, "licence": 0}
    os.makedirs(dest, exist_ok=True)
    try:
        with zipfile.ZipFile(io.BytesIO(got.stdout)) as z:
            for info in z.infolist():
                if info.is_dir():
                    continue
                # Drop the archive's top folder; refuse anything that tries to climb out.
                parts = [p for p in info.filename.replace("\\", "/").split("/")[1:] if p not in ("", ".")]
                if not parts or any(p == ".." or ":" in p for p in parts):
                    continue
                if any(p.lower() in SKIP_PARTS for p in parts[:-1]):
                    continue
                name = parts[-1].lower()
                what = None
                if name.endswith(".py") and info.file_size <= MAX_PY_BYTES:
                    what = "py"
                elif name.endswith(".ipynb") and info.file_size <= MAX_NOTEBOOK_BYTES:
                    what = "notebook"
                elif name.endswith((".js", ".mjs", ".cjs")) and info.file_size <= MAX_JS_BYTES and ".min." not in name \
                        and not name.endswith(("bundle.js", "-min.js")):
                    what = "js"
                elif len(parts) == 1 and name.split(".")[0] in LICENCE_NAMES and info.file_size <= MAX_LICENCE_BYTES:
                    what = "licence"
                if what is None:
                    continue
                data = z.read(info)
                if what == "notebook":
                    code = notebook_code(data)
                    if not code:
                        continue
                    data = code.encode("utf-8")
                    parts[-1] = parts[-1] + ".py"
                elif what == "js" and b"\n" not in data[:2000] and len(data) > 2000:
                    continue  # one enormous line: minified, whatever it is called
                target = os.path.join(dest, *parts)
                if not os.path.abspath(target).startswith(os.path.abspath(dest) + os.sep) or len(os.path.abspath(target)) > 250:
                    continue
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with open(target, "wb") as f:
                    f.write(data)
                kept[what] += 1
    except zipfile.BadZipFile:
        return repo, "failed: bad zip", 0
    except OSError as exc:
        return repo, f"failed: {type(exc).__name__}", 0
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump({"repo": repo, "url": row["GitHub URL"], "licence": row["License (verify)"],
                   "shelf": row["Domain shelf"], "description": row["GitHub description"],
                   "language": row["Primary language"], "fetched": "2026-11-23", "keeps": KEEPS,
                   "files_kept": kept}, f, ensure_ascii=False, indent=1)
    return repo, "ok", sum(kept.values())


def main():
    rows = selected()
    if len(sys.argv) > 1:
        rows = rows[: int(sys.argv[1])]
    os.makedirs(BERRIES, exist_ok=True)
    print(f"{len(rows)} repositories selected", flush=True)
    done = failed = files = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for repo, status, kept in pool.map(fetch, rows):
            done += 1
            files += kept
            if status.startswith("failed"):
                failed += 1
                print(f"  {repo}: {status}", flush=True)
            if done % 100 == 0:
                print(f"  {done}/{len(rows)} ...", flush=True)
    print(f"done: {done - failed} fetched or already present, {failed} failed, {files} files kept this run")


if __name__ == "__main__":
    main()
