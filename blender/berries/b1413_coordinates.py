# coordinates
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/graph/__init__.py, line 89
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import cos
from math import radians
from math import sin


def coordinates(x, y, distance, angle):
    return (
        (x + distance * cos(radians(angle))),
        (y + distance * sin(radians(angle)))
    )
