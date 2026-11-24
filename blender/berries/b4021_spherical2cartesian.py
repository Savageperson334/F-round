# spherical2cartesian
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 234
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cosd(deg):
    """ Cosine function with degree as input

    :param deg: Degree
    :type deg: float
    :return: Cosine value
    :rtype: float
    """
    rad = np.radians(deg)
    return np.cos(rad)


def sind(deg):
    """ Sine function with degree as input

    :param deg: Degree
    :type deg: float
    :return: Sine value
    :rtype: float
    """
    rad = np.radians(deg)
    return np.sin(rad)


def spherical2cartesian(lon, lat, dep):
    """ Convert spherical coordinates to cartesian coordinates

    :param lon: Longitude
    :type lon: float
    :param lat: Latitude
    :type lat: float
    :param dep: Depth
    :type dep: float
    :return: Cartesian coordinates
    :rtype: tuple
    """
    cola = 90. - lat
    r = 6371 - dep
    x = r * sind(cola) * cosd(lon)
    y = r * sind(cola) * sind(lon)
    z = r * cosd(cola)
    return x, y, z
