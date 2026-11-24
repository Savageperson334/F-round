# higher
#
# Copied verbatim from https://github.com/amacias/octo-vave
#   file tools/fm1_watch.py, line 69
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def ver_key(v):
    """Same comparison as the app's verKey: "v1.6.0" == "1.6", "V15" == "15"."""
    s = str(v or "").strip().lower()
    m = re.search(r"(\d+(?:\.\d+)+)(.*)$", s)
    if not m:
        return re.sub(r"^[^0-9]*", "", s) or s
    return re.sub(r"(\.0+)+$", "", m.group(1)) + re.sub(r"[\s()\[\]]", "", m.group(2))


def ver_nums(v):
    """Version numbers for ordering: "drum-v1.0.1" -> [1, 0, 1], "V16" -> [16]."""
    return [int(x) for x in re.findall(r"\d+", ver_key(v))]


def higher(a, b):
    """True when version a has a higher number than version b."""
    x, y = ver_nums(a), ver_nums(b)
    n = max(len(x), len(y))
    return x + [0] * (n - len(x)) > y + [0] * (n - len(y))
