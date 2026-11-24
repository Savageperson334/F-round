# angle_diff
#
# Copied verbatim from https://github.com/nion-software/nionswift
#   file nion/swift/model/Graphics.py, line 122
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def angle_diff(start_angle: float, end_angle: float) -> float:
    if end_angle > start_angle and end_angle - start_angle >= math.pi / 2:
        return (math.pi * 2 - end_angle + start_angle + math.pi * 2000) % (math.pi * 2)
    return (start_angle - end_angle + math.pi * 2000) % (math.pi * 2)
