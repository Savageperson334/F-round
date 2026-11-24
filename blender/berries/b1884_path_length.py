# path_length
#
# Copied verbatim from https://github.com/fogleman/axi
#   file axi/paths.py, line 18
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import hypot


def path_length(points):
    result = 0
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        result += hypot(x2 - x1, y2 - y1)
    return result
