# angle_between
#
# Copied verbatim from https://github.com/nion-software/nionswift
#   file nion/swift/model/Graphics.py, line 114
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def angle_between(n: float, a: float, b: float) -> bool:
    if a > b:
        return b < n < a
    if a < b:
        return math.pi * 2 > n > b or 0 < n < a
    return False
