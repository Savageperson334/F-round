# rad_to_quarterarcseconds
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file nexstar.py, line 61
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def rad_to_quarterarcseconds(rad: float) -> int:
    '''Convert an angle in radians to quarter arcseconds.'''
    quarterarcseconds_per_turn = 360 * 60 * 60 * 4
    return int(rad / (2 * math.pi) * quarterarcseconds_per_turn)
