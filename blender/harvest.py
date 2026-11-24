"""Harvest real, self-contained functions from the fetched repositories.

Reads every .py file under blender/_berries/ as TEXT (nothing is imported or
run) and keeps the top-level functions that are pure calculation: they use only
their own arguments, a short list of harmless builtins, a few maths-only
standard modules, literal constants of their own module, and other functions of
the same module that pass the same test.

That strict test is what makes it safe to run them later: a kept function has
no imports, no files, no network, no processes, no eval, no attribute names
beginning with an underscore, no classes, no globals.

The source of every kept function is copied VERBATIM, with the repository,
file, line and licence it came from.

Run from the repository root:  python -I blender/harvest.py
Writes blender/_work/harvest.json
"""
import ast
import hashlib
import json
import os
import shutil
import subprocess
import sys
import textwrap
import warnings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sandbox  # noqa: E402

# The repositories' own code triggers syntax warnings when parsed; they are not ours to fix.
warnings.simplefilter("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BERRIES = os.path.join(ROOT, "blender", "_berries")
OUT = os.path.join(ROOT, "blender", "_work", "harvest.json")
JS_HARVESTER = os.path.join(ROOT, "blender", "harvest_js.js")
JS_OUT = os.path.join(ROOT, "blender", "_work", "harvest_js.json")

# numpy, when it is installed: (top-level names allowed, {"linalg": names, "fft": names}). See sandbox.py.
NUMPY = sandbox.numpy_allowed()
NUMPY_SUBMODULES = ("numpy.linalg", "numpy.fft")
ATTR_DENY = sandbox.ATTR_DENY

# Modules a harvested function may use, and the names it may NOT take from them.
SAFE_MODULES = {
    "math": set(),
    "cmath": set(),
    "string": {"Formatter", "Template"},
    "itertools": set(),
    "operator": {"attrgetter", "methodcaller"},
    "functools": None,   # None: only the names in SAFE_FROM are allowed
    "fractions": set(),
    "statistics": set(),
    "colorsys": set(),
    "bisect": set(),
    "heapq": set(),
    "re": set(),
    "json": {"load", "dump"},
    "collections": set(),
    "struct": set(),
    "base64": set(),
    "binascii": set(),
    "hashlib": {"file_digest"},
    "unicodedata": set(),
    "textwrap": set(),
    "decimal": set(),
    "copy": set(),
}
SAFE_FROM = {"functools": {"reduce", "partial"}}

SAFE_BUILTINS = set(sandbox.SAFE_BUILTINS) | {"True", "False", "None", "print"}

ALLOWED_NODES = (
    ast.Expr, ast.Assign, ast.AugAssign, ast.AnnAssign, ast.Return, ast.If, ast.For, ast.While, ast.Break,
    ast.Continue, ast.Pass, ast.Try, ast.ExceptHandler, ast.Raise, ast.Assert, ast.BinOp, ast.UnaryOp,
    ast.BoolOp, ast.Compare, ast.Call, ast.Name, ast.Constant, ast.List, ast.Tuple, ast.Dict, ast.Set,
    ast.Subscript, ast.Slice, ast.Attribute, ast.IfExp, ast.ListComp, ast.SetComp, ast.DictComp,
    ast.GeneratorExp, ast.comprehension, ast.Lambda, ast.JoinedStr, ast.FormattedValue, ast.Starred,
    ast.keyword, ast.NamedExpr, ast.arguments, ast.arg, ast.FunctionDef, ast.Delete, ast.Del,
    ast.Load, ast.Store, ast.operator, ast.unaryop, ast.boolop, ast.cmpop, ast.expr_context,
)

SKIP_PATH_PARTS = {"test", "tests", "testing", "docs", "doc", "venv", ".venv", "site-packages", "build", "dist",
                   "node_modules", "migrations", "__pycache__"}
MAX_FILE_BYTES = 400_000
MIN_LINES, MAX_LINES = 3, 120
MAX_PARAMS = 4
MAX_CONST_CHARS = 6000


class Module:
    """One source file: what it imports, its literal constants, its functions."""

    def __init__(self, tree):
        self.aliases = {}       # local name -> ("module", modname) or ("name", modname, attr)
        self.import_lines = {}  # local name -> the line of source we will reproduce
        self.constants = {}     # name -> ast.Assign
        self.functions = {}     # name -> ast.FunctionDef
        for node in tree.body:
            if isinstance(node, ast.Import):
                for a in node.names:
                    if a.name in SAFE_MODULES or (NUMPY and (a.name == "numpy" or (a.name in NUMPY_SUBMODULES and a.asname))):
                        local = a.asname or a.name
                        self.aliases[local] = ("module", a.name)
                        self.import_lines[local] = f"import {a.name}" + (f" as {a.asname}" if a.asname else "")
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and NUMPY and (node.module == "numpy" or node.module in NUMPY_SUBMODULES):
                for a in node.names:
                    local = a.asname or a.name
                    if node.module == "numpy" and a.name in ("linalg", "fft"):
                        self.aliases[local] = ("module", "numpy." + a.name)
                    elif node.module == "numpy" and a.name in NUMPY[0]:
                        self.aliases[local] = ("name", "numpy", a.name)
                    elif node.module != "numpy" and a.name in NUMPY[1][node.module.split(".")[1]]:
                        self.aliases[local] = ("name", node.module, a.name)
                    else:
                        continue
                    self.import_lines[local] = f"from {node.module} import {a.name}" + (f" as {a.asname}" if a.asname else "")
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module in SAFE_MODULES:
                banned = SAFE_MODULES[node.module]
                for a in node.names:
                    if a.name == "*" or a.name.startswith("_"):
                        continue
                    if banned is None:
                        if a.name not in SAFE_FROM.get(node.module, set()):
                            continue
                    elif a.name in banned:
                        continue
                    local = a.asname or a.name
                    self.aliases[local] = ("name", node.module, a.name)
                    self.import_lines[local] = f"from {node.module} import {a.name}" + (f" as {a.asname}" if a.asname else "")
            elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                self.constants[node.targets[0].id] = node
            elif isinstance(node, ast.FunctionDef):
                self.functions[node.name] = node


def stored_names(fn):
    """Every name the function itself binds: parameters, assignments, loop and comprehension targets."""
    names = set()
    for node in ast.walk(fn):
        if isinstance(node, ast.arg):
            names.add(node.arg)
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            names.add(node.id)
        elif isinstance(node, ast.ExceptHandler) and node.name:
            names.add(node.name)
        elif isinstance(node, ast.FunctionDef) and node is not fn:
            names.add(node.name)
    return names


def check_expression_nodes(root, why):
    """Structural rules shared by functions and constants. Returns False (and a reason) on the first breach."""
    for node in ast.walk(root):
        if not isinstance(node, ALLOWED_NODES):
            why.append(type(node).__name__)
            return False
        if isinstance(node, ast.Attribute):
            if node.attr.startswith("_"):
                why.append("underscore attribute")
                return False
        elif isinstance(node, ast.Name) and node.id.startswith("__"):
            why.append("dunder name")
            return False
        elif isinstance(node, ast.FunctionDef):
            if node.decorator_list or node.args.vararg or node.args.kwarg:
                why.append("decorated or variadic")
                return False
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "type" and (len(node.args) != 1 or node.keywords):
                why.append("type() used to build a class")
                return False
        elif isinstance(node, ast.Constant) and isinstance(node.value, (bytes,)):
            why.append("bytes literal")
            return False
    return True


def free_names(root, bound):
    """Names read but not bound inside `root`."""
    out = set()
    for node in ast.walk(root):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load) and node.id not in bound:
            out.add(node.id)
    return out


def module_attribute_ok(module, root):
    """math.sin is fine; operator.attrgetter, np.load, x.tofile and a module handed around whole are not."""
    bound = stored_names(root) if isinstance(root, ast.FunctionDef) else set()
    modules = {local: alias[1] for local, alias in module.aliases.items() if alias[0] == "module"}
    if any(local in bound and name.startswith("numpy") for local, name in modules.items()):
        return False   # a local variable hiding numpy's name: too easy to misjudge, leave it
    submodule_refs, consumed, proper_uses = {}, set(), set()
    for node in ast.walk(root):
        if not isinstance(node, ast.Attribute):
            continue
        if node.attr in ATTR_DENY:
            return False
        if isinstance(node.value, ast.Name) and node.value.id in modules and node.value.id not in bound:
            proper_uses.add(id(node.value))
            name = modules[node.value.id]
            if name == "numpy":
                if node.attr in ("linalg", "fft"):
                    submodule_refs[id(node)] = node.attr
                elif node.attr not in NUMPY[0]:
                    return False
            elif name in NUMPY_SUBMODULES:
                if node.attr not in NUMPY[1][name.split(".")[1]]:
                    return False
            else:
                banned = SAFE_MODULES[name]
                if banned is None:
                    if node.attr not in SAFE_FROM.get(name, set()):
                        return False
                elif node.attr in banned:
                    return False
    for node in ast.walk(root):
        if isinstance(node, ast.Attribute) and id(node.value) in submodule_refs:
            if node.attr not in NUMPY[1][submodule_refs[id(node.value)]]:
                return False
            consumed.add(id(node.value))
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load) and node.id in modules and node.id not in bound:
            if id(node) not in proper_uses:
                return False   # the module itself passed somewhere, not one of its names
    return len(consumed) == len(submodule_refs)


class Judge:
    """Decides, per module, which functions and constants are admissible, following dependencies."""

    def __init__(self, module, source):
        self.m = module
        self.source = source
        self.fn_verdict = {}     # name -> None (in progress) | False | dict(deps, consts, imports)
        self.const_verdict = {}

    def constant(self, name, trail=()):
        if name in self.const_verdict:
            return self.const_verdict[name]
        node = self.m.constants.get(name)
        verdict = False
        if node is not None and name not in trail:
            text = ast.get_source_segment(self.source, node) or ""
            why = []
            if 0 < len(text) <= MAX_CONST_CHARS and check_expression_nodes(node.value, why) and module_attribute_ok(self.m, node.value):
                needs_consts, needs_imports, ok = [], [], True
                for free in free_names(node.value, set()):
                    if free in SAFE_BUILTINS:
                        continue
                    if free in self.m.aliases:
                        needs_imports.append(free)
                    elif free in self.m.constants and self.constant(free, trail + (name,)):
                        needs_consts.append(free)
                    else:
                        ok = False
                        break
                if ok:
                    verdict = {"consts": needs_consts, "imports": needs_imports, "text": text}
        self.const_verdict[name] = verdict
        return verdict

    def function(self, name):
        if name in self.fn_verdict:
            # A function already being judged further up the chain: allow the cycle (recursion).
            return self.fn_verdict[name] if self.fn_verdict[name] is not None else {"deps": [], "consts": [], "imports": []}
        fn = self.m.functions.get(name)
        if fn is None:
            return False
        self.fn_verdict[name] = None
        verdict = self._judge(fn)
        self.fn_verdict[name] = verdict
        return verdict

    def _judge(self, fn):
        if fn.decorator_list or fn.args.vararg or fn.args.kwarg or fn.args.kwonlyargs or fn.args.posonlyargs:
            return False
        why = []
        if not check_expression_nodes(fn, why) or not module_attribute_ok(self.m, fn):
            return False
        for default in fn.args.defaults:
            try:
                ast.literal_eval(default)
            except Exception:  # noqa: BLE001
                return False
        bound = stored_names(fn)
        deps, consts, imports = [], [], []
        for free in sorted(free_names(fn, bound)):
            if free in SAFE_BUILTINS:
                continue
            if free in self.m.aliases:
                imports.append(free)
            elif free in self.m.functions:
                if not self.function(free):
                    return False
                deps.append(free)
            elif self.constant(free):
                consts.append(free)
            else:
                return False
        return {"deps": deps, "consts": consts, "imports": imports}


def has_real_return(fn):
    for node in ast.walk(fn):
        if isinstance(node, ast.Return) and node.value is not None:
            if not (isinstance(node.value, ast.Constant) and node.value.value is None):
                return True
    return False


def closure(judge, name):
    """Everything a function needs, in dependency order: imports, constants, helper functions."""
    imports, consts, helpers = [], [], []
    seen_fn, seen_const = set(), set()

    def add_const(c):
        if c in seen_const:
            return
        seen_const.add(c)
        v = judge.const_verdict[c]
        for i in v["imports"]:
            if i not in imports:
                imports.append(i)
        for sub in v["consts"]:
            add_const(sub)
        consts.append(c)

    def add_fn(f, is_root):
        if f in seen_fn:
            return
        seen_fn.add(f)
        v = judge.fn_verdict[f]
        for i in v["imports"]:
            if i not in imports:
                imports.append(i)
        for c in v["consts"]:
            add_const(c)
        for d in v["deps"]:
            add_fn(d, False)
        if not is_root:
            helpers.append(f)

    add_fn(name, True)
    return imports, consts, helpers


def harvest_file(path, rel, berry, out, stats):
    try:
        if os.path.getsize(path) > MAX_FILE_BYTES:
            return
        source = open(path, encoding="utf-8", errors="strict").read()
        tree = ast.parse(source)
    except Exception:  # noqa: BLE001
        stats["unreadable files"] += 1
        return
    stats["files read"] += 1
    module = Module(tree)
    judge = Judge(module, source)
    for name, fn in module.functions.items():
        stats["functions seen"] += 1
        if name.startswith("_") or name.startswith("test") or name == "main":
            continue
        params = [a.arg for a in fn.args.args]
        required = len(params) - len(fn.args.defaults)
        if not 1 <= required <= MAX_PARAMS or len(params) > MAX_PARAMS + 3:
            continue
        lines = (fn.end_lineno or fn.lineno) - fn.lineno + 1
        if not MIN_LINES <= lines <= MAX_LINES or not has_real_return(fn):
            continue
        if not judge.function(name):
            continue
        imports, consts, helpers = closure(judge, name)
        text = ast.get_source_segment(source, fn)
        if not text:
            continue
        doc = (ast.get_docstring(fn) or "").strip().split("\n")[0][:200]
        body_print = hashlib.md5(ast.dump(ast.Module(body=fn.body, type_ignores=[])).encode()).hexdigest()
        import_lines = [module.import_lines[i] for i in imports]
        out.append({
            "lang": "py", "numpy": any("numpy" in line for line in import_lines),
            "repo": berry["repo"], "shelf": berry["shelf"], "licence": berry["licence"], "url": berry["url"],
            "file": rel.replace("\\", "/"), "line": fn.lineno, "name": name, "params": params, "required": required,
            "doc": doc, "source": textwrap.dedent(text),
            "imports": import_lines,
            "consts": [{"name": c, "source": judge.const_verdict[c]["text"]} for c in consts],
            "helpers": [{"name": h, "source": textwrap.dedent(ast.get_source_segment(source, module.functions[h]) or "")} for h in helpers],
            "body_print": body_print,
        })
        stats["functions kept"] += 1


def main():
    stats = {"repositories": 0, "files read": 0, "unreadable files": 0, "functions seen": 0, "functions kept": 0}
    out = []
    for folder in sorted(os.listdir(BERRIES)):
        meta_path = os.path.join(BERRIES, folder, "_berry.json")
        if not os.path.exists(meta_path):
            continue
        berry = json.load(open(meta_path, encoding="utf-8"))
        stats["repositories"] += 1
        base = os.path.join(BERRIES, folder)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d.lower() not in SKIP_PATH_PARTS and not d.startswith(".")]
            for filename in filenames:
                low = filename.lower()
                if not low.endswith(".py") or low.startswith("test_") or low.endswith("_test.py") or low in ("setup.py", "conftest.py"):
                    continue
                full = os.path.join(dirpath, filename)
                harvest_file(full, os.path.relpath(full, base), berry, out, stats)

    # The JavaScript half, read by Node (parsed as text there too, never run).
    if shutil.which("node") and os.path.isdir(os.path.join(ROOT, "blender", "_work", "node", "node_modules", "acorn")):
        got = subprocess.run(["node", "--max-old-space-size=2048", JS_HARVESTER, BERRIES, JS_OUT], capture_output=True, text=True)
        if got.returncode == 0:
            js = json.load(open(JS_OUT, encoding="utf-8"))
            out.extend(js["functions"])
            stats["javascript"] = js["stats"]
        else:
            print("JavaScript harvest failed:", got.stderr[-400:])
    else:
        print("JavaScript left out: needs node, and acorn installed in blender/_work/node")

    # The same function body in several repositories is one function with several homes.
    by_body = {}
    unique = []
    for f in out:
        first = by_body.get(f["body_print"])
        if first is None:
            f["id"] = len(unique)
            f["also_in"] = []
            by_body[f["body_print"]] = f
            unique.append(f)
        elif f["repo"] != first["repo"] and f["repo"] not in first["also_in"]:
            first["also_in"].append(f["repo"])
    for f in unique:
        del f["body_print"]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"stats": stats, "functions": unique}, fh, ensure_ascii=False)
    repos_with = len({f["repo"] for f in unique})
    print(stats)
    print({"python": sum(1 for f in unique if f["lang"] == "py"), "of which use numpy": sum(1 for f in unique if f.get("numpy")),
           "from notebooks": sum(1 for f in unique if f["file"].endswith(".ipynb.py")),
           "javascript": sum(1 for f in unique if f["lang"] == "js")})
    print(f"{len(unique)} distinct functions from {repos_with} repositories; "
          f"{sum(1 for f in unique if f['also_in'])} appear in more than one repository")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
