# rad2deg
#
# Copied verbatim from https://github.com/MGross21/armctl
#   file armctl/utils/units.py, line 27
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def rad2deg(radians: float) -> float:
    """Convert radians to degrees."""
    return math.degrees(radians)
