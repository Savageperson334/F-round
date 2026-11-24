# depth
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/effects/ladder/make_tables.py, line 52
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def lookup(fn, k):
    """The 65-entry interpolated lookup the original ColdFire handler used."""
    if k == 127:
        return fn(127)
    v = fn(2 * (k // 2))
    return (v + fn(min(127, 2 * (k // 2) + 2))) // 2 if k & 1 else v


def depth(k):           # ENVA: bipolar, 64 neutral
    def fn(k):
        d = k - 64
        if not d:
            return 0
        limit = 64 if d < 0 else 63
        return (-1 if d < 0 else 1) * round(limit * 73728 * math.expm1(4 * abs(d) / limit) / math.expm1(4))
    return lookup(fn, k)
