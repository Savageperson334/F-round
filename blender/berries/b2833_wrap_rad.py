# wrap_rad
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file util.py, line 48
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def wrap_rad(theta: float, minimum: float) -> float:
    '''
    Add or subtract multiples of 2*pi until the angle
    theta is between minimum and minimum+2*pi.
    '''
    while theta >= minimum + 2 * math.pi:
        theta -= 2 * math.pi
    while theta < minimum:
        theta += 2 * math.pi
    return theta
