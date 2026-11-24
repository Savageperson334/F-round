# km2deg
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 90
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def km2deg(km):
    """ Convert km to degree

    :param km: Distance in km
    :type km: float
    :return: Distance in degree
    :rtype: float
    """
    radius = 6371
    circum = 2*np.pi*radius
    conv = circum / 360
    deg = km / conv
    return deg
