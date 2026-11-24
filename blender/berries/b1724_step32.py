# step32
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file ci/ladder_check.py, line 80
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def step32(d):
    """d / 32 rounded toward zero."""
    return d >> 5 if d >= 0 else -((-d) >> 5)
