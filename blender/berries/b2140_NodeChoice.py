# NodeChoice
#
# Copied verbatim from https://github.com/gvard/astrodata
#   file src/astrodata/solarsystem/deltav.py, line 189
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def NodeChoice(
    w: float, ec: float, a: float
) -> float:  # which node was chosen, for all future calculation the periapsis direction is defined as 0 degrees
    Node1 = a * (1 - (ec**2)) / (1 + ec * math.cos(-w))
    Node2 = a * (1 - (ec**2)) / (1 + ec * math.cos(math.pi - w))
    if Node1 > Node2:
        return -w
    else:
        return math.pi - w
