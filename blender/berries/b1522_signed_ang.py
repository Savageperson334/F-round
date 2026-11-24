# signed_ang
#
# Copied verbatim from https://github.com/computational-imaging/neural-3d-holography
#   file utils.py, line 413
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#   the same function also appears in: computational-imaging/time-multiplexed-neural-holography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def signed_ang(angle):
    """
    cast all angles into [-pi, pi]
    """
    return (angle + math.pi) % (2*math.pi) - math.pi
