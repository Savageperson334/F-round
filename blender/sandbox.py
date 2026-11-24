"""Load a harvested function so it can be called, with nothing else in reach.

A harvested function has already passed the harvester's test (no imports,
files, network, processes, eval, classes or underscore attributes). This is the
second lock.

Python: its source is executed in a namespace whose builtins are only a short
harmless list, with only the modules it asked for. numpy is handed over as a
cut-down copy holding only the names the harvester allows (no file reading or
writing, no submodules but linalg and fft).

JavaScript: it is run by Node inside an empty context with code generation
from strings switched off and a time limit on every call (js_runner.js), in a
Node process started without permission to write files or start processes.

Values cross between functions as plain JSON: numbers, text, lists, dicts.
"""
import builtins
import importlib
import json
import os
import subprocess
import types
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))

SAFE_MODULES = ("math", "cmath", "string", "itertools", "operator", "functools", "fractions", "statistics",
                "colorsys", "bisect", "heapq", "re", "json", "collections", "struct", "base64", "binascii",
                "hashlib", "unicodedata", "textwrap", "decimal", "copy")
NUMPY_MODULES = ("numpy", "numpy.linalg", "numpy.fft")
## numpy names a harvested function may not use: anything that reads or writes files, changes
## numpy's global behaviour, prints, or looks things up by name in the caller.
NUMPY_DENY = {
    "load", "save", "savez", "savez_compressed", "savetxt", "loadtxt", "genfromtxt", "fromfile", "fromregex",
    "memmap", "DataSource", "test", "show_config", "show_runtime", "info", "source", "lookfor", "get_include",
    "seterr", "seterrcall", "setbufsize", "getbufsize", "geterr", "geterrcall", "set_printoptions", "printoptions",
    "errstate", "frombuffer", "from_dlpack", "fromstring", "bmat", "safe_eval", "deprecate", "who", "byte_bounds",
    "add_newdoc", "add_docstring", "add_newdoc_ufunc", "set_string_function", "Tester", "open_memmap",
    "get_printoptions", "typename", "mintypecode",
}
## Attribute names no harvested function may touch, whatever they are on (array.tofile, json.dump ...).
ATTR_DENY = {"tofile", "dump", "ctypes", "setflags", "save", "savez", "savetxt", "memmap", "fromfile", "loadtxt",
             "genfromtxt", "fromregex", "load", "savefig", "show", "write", "read", "open", "system", "popen"}

SAFE_BUILTINS = (
    "abs", "all", "any", "bin", "bool", "callable", "chr", "complex", "dict", "divmod", "enumerate", "filter",
    "float", "format", "frozenset", "hasattr", "hex", "int", "isinstance", "iter", "len", "list", "map", "max",
    "min", "next", "oct", "ord", "pow", "range", "repr", "reversed", "round", "set", "slice", "sorted", "str",
    "sum", "tuple", "zip", "type",
    "ValueError", "TypeError", "ZeroDivisionError", "IndexError", "KeyError", "Exception", "RuntimeError",
    "ArithmeticError", "OverflowError", "StopIteration", "AssertionError", "NotImplementedError", "LookupError",
    "AttributeError", "FloatingPointError",
)
_BUILTINS = {name: getattr(builtins, name) for name in SAFE_BUILTINS}
_BUILTINS.update({"True": True, "False": False, "None": None, "print": lambda *args, **kwargs: None})

_numpy = None        # the real module, once something needs it
_facade = None       # the cut-down copy handed to harvested functions
_numpy_names = None


def numpy_allowed():
    """(top-level names, {"linalg": names, "fft": names}) a harvested function may use, or None without numpy."""
    global _numpy, _numpy_names
    if _numpy_names is None:
        try:
            _numpy = importlib.import_module("numpy")
        except ImportError:
            _numpy_names = False
            return None
        _numpy.seterr(all="ignore")
        warnings.simplefilter("ignore")
        top = {n for n in dir(_numpy) if not n.startswith("_") and n not in NUMPY_DENY
               and not isinstance(getattr(_numpy, n), types.ModuleType)}
        sub = {}
        for m in ("linalg", "fft"):
            module = getattr(_numpy, m)
            sub[m] = {n for n in dir(module) if not n.startswith("_") and n not in NUMPY_DENY
                      and not isinstance(getattr(module, n), types.ModuleType)}
        _numpy_names = (top, sub)
    return _numpy_names or None


def numpy_facade():
    global _facade
    if _facade is None:
        allowed = numpy_allowed()
        if allowed is None:
            raise ValueError("numpy is not installed")
        top, sub = allowed
        _facade = types.SimpleNamespace(**{n: getattr(_numpy, n) for n in top})
        for m, names in sub.items():
            setattr(_facade, m, types.SimpleNamespace(**{n: getattr(getattr(_numpy, m), n) for n in names}))
    return _facade


def _module(name):
    if name in NUMPY_MODULES:
        facade = numpy_facade()
        return facade if name == "numpy" else getattr(facade, name.split(".")[1])
    if name in SAFE_MODULES:
        return importlib.import_module(name)
    raise ValueError("module not allowed: " + name)


def _bind_import(line, namespace):
    words = line.split()
    if words[0] == "import":                      # import math [as m]
        if len(words) == 2 and "." in words[1]:
            raise ValueError("import not allowed: " + line)
        namespace[words[3] if len(words) == 4 else words[1]] = _module(words[1])
    elif words[0] == "from":                      # from math import sin [as s]
        name = words[3]
        if name.startswith("_") or name in ATTR_DENY:
            raise ValueError("import not allowed: " + line)
        namespace[words[5] if len(words) == 6 else name] = getattr(_module(words[1]), name)
    else:
        raise ValueError("not an import: " + line)


# ------------------------------------------------------------- crossing over

def plain(value, depth=0):
    """A function's result as plain Python: numpy arrays and numbers become lists and numbers."""
    module = type(value).__module__
    if module == "numpy" and _numpy is not None:
        if isinstance(value, _numpy.ndarray):
            if value.size > 4000 or value.ndim > 3 or value.dtype.kind not in "biufU":
                return _Unusable
            return value.tolist()
        if isinstance(value, _numpy.generic):
            return plain(value.item(), depth + 1) if depth < 4 else _Unusable
        return _Unusable
    if isinstance(value, (list, tuple)) and depth < 4 and len(value) <= 4000:
        return [plain(v, depth + 1) for v in value]
    if isinstance(value, dict) and depth < 4 and len(value) <= 500:
        return {k: plain(v, depth + 1) for k, v in value.items()}
    return value


class _Unusable:
    """Stands for a result that is too big or too odd to pass on."""


def dress(value):
    """A list of numbers, or a rectangular table of them, as the numpy array a numpy function expects."""
    if kind(value) in ("nums", "table"):
        try:
            return _numpy.array(value, dtype=float)
        except Exception:  # noqa: BLE001
            return value
    return value


def js_code(function):
    """The JavaScript a harvested function needs, in order: constants, helpers, itself."""
    parts = [c["source"] for c in function["consts"]] + [h["source"] for h in function["helpers"]] + [function["source"]]
    return "\n;\n".join(parts)


def load(function, bridge=None):
    """Return the callable for one harvest.json entry. Its results come back as plain values."""
    if function.get("lang") == "js":
        if bridge is None:
            raise ValueError("no JavaScript bridge")
        return bridge.function(function["id"], function["name"], js_code(function))
    namespace = {"__builtins__": dict(_BUILTINS)}
    for line in function["imports"]:
        _bind_import(line, namespace)
    for const in function["consts"]:
        exec(compile(const["source"], "<berry const>", "exec"), namespace)
    for helper in function["helpers"]:
        exec(compile(helper["source"], "<berry helper>", "exec"), namespace)
    exec(compile(function["source"], "<berry>", "exec"), namespace)
    return wrap(namespace[function["name"]], bool(function.get("numpy")))


def wrap(fn, uses_numpy):
    if uses_numpy:
        numpy_allowed()

        def call(*args):
            return plain(fn(*[dress(a) for a in args]))
    else:
        def call(*args):
            return plain(fn(*args))
    return call


class NodeBridge:
    """Runs JavaScript functions in a locked-down Node process, one JSON line per call."""

    def __init__(self, timeout_ms=800):
        self.timeout_ms = timeout_ms
        self.proc = None
        self.loaded = set()
        self.dead = set()

    def _start(self):
        runner = os.path.join(HERE, "js_runner.js")
        self.proc = subprocess.Popen(
            ["node", "--max-old-space-size=512", "--permission", "--allow-fs-read=" + HERE, runner, str(self.timeout_ms)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, encoding="utf-8", bufsize=1)
        self.loaded = set()

    def _ask(self, message):
        if self.proc is None or self.proc.poll() is not None:
            self._start()
        try:
            self.proc.stdin.write(json.dumps(message) + "\n")
            self.proc.stdin.flush()
            line = self.proc.stdout.readline()
        except OSError:
            line = ""
        if not line:
            self.close()
            raise RuntimeError("node stopped")
        return json.loads(line)

    def function(self, key, name, code):
        def call(*args):
            if key in self.dead:
                raise RuntimeError("set aside")
            try:
                if key not in self.loaded:
                    if not self._ask({"load": key, "name": name, "code": code}).get("ok"):
                        self.dead.add(key)
                        raise ValueError("will not load")
                    self.loaded.add(key)
                reply = self._ask({"call": key, "args": json.dumps(args)})
            except RuntimeError:
                self.dead.add(key)   # it took Node down with it: never again
                raise
            if not reply.get("ok"):
                raise ValueError("failed")
            return json.loads(reply["value"])
        return call

    def close(self):
        if self.proc is not None:
            try:
                self.proc.kill()
            except OSError:
                pass
        self.proc = None
        self.loaded = set()


# ---------------------------------------------------------------- kinds

def _number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def kind(value):
    """The shape of a value, as far as fitting one function to another goes."""
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "str"
    if isinstance(value, (list, tuple)):
        if not value:
            return "empty"
        if all(_number(v) for v in value):
            return "nums"
        if all(isinstance(v, str) for v in value):
            return "strs"
        if all(isinstance(v, (list, tuple)) and v and all(_number(x) for x in v) for v in value):
            return "table"
        return "seq"
    if isinstance(value, dict):
        return "dict"
    if value is None:
        return "none"
    return "other"


## What an output of one kind may be fed to.
FITS = {
    "int": ("int", "float"), "float": ("float",), "str": ("str",), "nums": ("nums",), "strs": ("strs",),
    "table": ("table",), "bool": ("bool", "int"), "dict": ("dict",),
}


def tame(value, depth=0):
    """True when a value is small and plain enough to pass on and to print."""
    if isinstance(value, bool) or value is None:
        return True
    if isinstance(value, int):
        return abs(value) < 10 ** 18
    if isinstance(value, float):
        return value == value and abs(value) < 1e18
    if isinstance(value, str):
        return len(value) <= 4000
    if isinstance(value, (list, tuple)):
        return depth < 3 and len(value) <= 2000 and all(tame(v, depth + 1) for v in value)
    if isinstance(value, dict):
        return depth < 3 and len(value) <= 500 and all(isinstance(k, (str, int, float)) and tame(v, depth + 1) for k, v in value.items())
    return False
