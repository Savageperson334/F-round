# srad2skm
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 156
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


def srad2skm(srad):
    """ Convert s/rad to s/km

    :param srad: s/rad
    :type srad: float
    :return: s/km
    :rtype: float
    """
    sdeg = srad * ((2*np.pi)/360)
    return sdeg / deg2km(1)
