# s56
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file ci/ladder_check.py, line 53
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def s56(v):
    v &= (1 << 56) - 1
    return v - (1 << 56) if v >> 55 else v
