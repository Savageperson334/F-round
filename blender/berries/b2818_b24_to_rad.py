# b24_to_rad
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file nexstar.py, line 52
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def b24_to_rad(b24: int) -> float:
    '''Convert an angle in the 24 bit representation the NexStar serial protocol likes to radians.'''
    return b24/(2**24)*2*math.pi
