# fb_mantissa
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 1817
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fb_mantissa(i):
    n=((i<<15)+134217728)<<3
    n=(n*n+(1<<31))>>32
    n=(((n*715827883+(1<<31))>>32)<<3)+715827882
    return n>>8
