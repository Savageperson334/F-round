# cartesian2spherical
#
# Copied verbatim from https://github.com/xaviermouy/ecosound
#   file ecosound/localization/archive/initial_tes.py, line 185
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as np


def cartesian2spherical(x,y,z):
    # Converting cartesian to polar coordinate
    const = 180/np.pi
    XsqPlusYsq = x**2 + y**2
    r = math.sqrt(XsqPlusYsq + z**2)               # r
    elev = math.atan2(math.sqrt(XsqPlusYsq),z)     # theta
    az = math.atan2(y,x)*180/np.pi
    return r, az, elev
