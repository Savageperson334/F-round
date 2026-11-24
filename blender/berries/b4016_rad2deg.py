# rad2deg
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 120
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rad2deg(rad):
    """ Convert radian to degree

    :param rad: Radian
    :type rad: float
    :return: Degree
    :rtype: float
    """
    deg = rad*(360/(2*np.pi))
    return deg
