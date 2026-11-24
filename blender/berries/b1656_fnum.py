# fnum
#
# Copied verbatim from https://github.com/ductone/orrery
#   file research/modelbench/fetch.py, line 302
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fnum(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(",", "").replace("$", "").replace("%", "")
    if not s or s.lower() in ("nan", "none", "null", "-", "n/a"):
        return None
    try:
        x = float(s)
    except ValueError:
        return None
    if x != x:
        return None
    return x
