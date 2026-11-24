# s24
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file ci/ladder_check.py, line 48
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

Q = 1 << 23


def s24(v):
    v &= 0xffffff
    return v - (1 << 24) if v & Q else v
