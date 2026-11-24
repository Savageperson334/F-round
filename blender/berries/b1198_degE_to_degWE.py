# degE_to_degWE
#
# Copied verbatim from https://github.com/brodeau/gonzag
#   file gonzag/utils.py, line 24
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import copysign
import numpy as nmp


def degE_to_degWE( X ):
    '''
    # From longitude in 0 -- 360 frame to -180 -- +180 frame...
    '''
    if nmp.shape( X ) == ():
        # X is a scalar
        return     copysign(1., 180.-X)*        min(X,     abs(X-360.))
    else:
        # X is an array
        return nmp.copysign(1., 180.-X)*nmp.minimum(X, nmp.abs(X-360.))
