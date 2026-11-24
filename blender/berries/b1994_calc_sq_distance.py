# calc_sq_distance
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/geometry/curves.py, line 68
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def calc_sq_distance( x1,y1, x2,y2 ):
    dx = x2-x1
    dy = y2-y1
    return dx * dx + dy * dy
