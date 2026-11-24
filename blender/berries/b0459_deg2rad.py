# deg2rad
#
# Copied verbatim from https://github.com/MGross21/armctl
#   file armctl/utils/units.py, line 22
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def deg2rad(degrees: float) -> float:
    """Convert degrees to radians."""
    return math.radians(degrees)
