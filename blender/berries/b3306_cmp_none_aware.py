# cmp_none_aware
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gf/seismosizer.py, line 72
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def cmp_none_aware(a, b):
    if isinstance(a, tuple) and isinstance(b, tuple):
        for xa, xb in zip(a, b):
            rv = cmp_none_aware(xa, xb)
            if rv != 0:
                return rv

        return 0

    anone = a is None
    bnone = b is None

    if anone and bnone:
        return 0

    if anone:
        return -1

    if bnone:
        return 1

    return bool(a > b) - bool(a < b)
