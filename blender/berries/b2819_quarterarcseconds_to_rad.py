# quarterarcseconds_to_rad
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file nexstar.py, line 56
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def quarterarcseconds_to_rad(quarterarcseconds: int | float) -> float:
    '''Convert an angle in quarter arcseconds to radians.'''
    quarterarcseconds_per_turn = 360 * 60 * 60 * 4
    return quarterarcseconds / quarterarcseconds_per_turn * 2 * math.pi
