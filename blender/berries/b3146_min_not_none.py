# min_not_none
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/cake.py, line 4378
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def min_not_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)
