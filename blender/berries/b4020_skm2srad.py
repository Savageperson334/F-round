# skm2srad
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 168
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def deg2km(deg):
    """ Convert degree to km

    :param deg: Distance in degree
    :type deg: float
    :return: Distance in km
    :rtype: float
    """
    radius = 6371
    circum = 2*np.pi*radius
    conv = circum / 360
    km = deg * conv
    return km


def rad2deg(rad):
    """ Convert radian to degree

    :param rad: Radian
    :type rad: float
    :return: Degree
    :rtype: float
    """
    deg = rad*(360/(2*np.pi))
    return deg


def skm2srad(skm):
    """ Convert s/km to s/rad

    :param skm: s/km
    :type skm: float
    :return: s/rad
    :rtype: float
    """
    sdeg = skm * deg2km(1)
    return rad2deg(sdeg)
