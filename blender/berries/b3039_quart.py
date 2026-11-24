# quart
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/velo_fit.py, line 40
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def quart(v):
    v = sorted(v)
    n = len(v)
    return v[n // 4], v[n // 2], v[(3 * n) // 4]
