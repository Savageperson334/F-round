# joints2rad
#
# Copied verbatim from https://github.com/MGross21/armctl
#   file armctl/utils/units.py, line 63
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def joints2rad(joint_positions):
    """
    Convert joint positions from degrees to radians.
    Accepts either a list of floats or a list of (min, max) tuples.
    """
    if not joint_positions:
        return []

    if isinstance(joint_positions[0], (tuple, list)):
        return [(math.radians(jmin), math.radians(jmax)) for jmin, jmax in joint_positions]
    return [math.radians(j) for j in joint_positions]
