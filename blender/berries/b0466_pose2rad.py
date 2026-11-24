# pose2rad
#
# Copied verbatim from https://github.com/MGross21/armctl
#   file armctl/utils/units.py, line 83
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def pose2rad(pose: list[float]) -> list[float]:
    """Convert pose orientation (last 3 elements) from degrees to radians."""
    if len(pose) < 6:
        raise ValueError("Pose must have at least 6 elements (x, y, z, rx, ry, rz)")
    return pose[:3] + [math.radians(a) for a in pose[3:]]
