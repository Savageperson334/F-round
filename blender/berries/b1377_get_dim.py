# get_dim
#
# Copied verbatim from https://github.com/citiesskylines-csur/CSUR
#   file graphics/graphics.py, line 14
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_dim(polygon):
    xs = [p[0] for p in polygon]
    ys = [p[1] for p in polygon]
    return max(xs) - min(xs), max(ys) - min(ys)
