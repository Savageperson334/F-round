# TwistAng
#
# Copied verbatim from https://github.com/gvard/astrodata
#   file src/astrodata/solarsystem/deltav.py, line 156
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def TwistAng(w: float, i: float) -> float:  # angle for very last maneuver
    return math.acos(
        math.cos(i)
        / math.sqrt((math.cos(w) ** 2) + ((math.cos(i) ** 2) * (math.sin(w) ** 2)))
    )
