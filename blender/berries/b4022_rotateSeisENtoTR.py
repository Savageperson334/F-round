# rotateSeisENtoTR
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 254
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


def rotateSeisENtoTR(e, n, baz):
    """ Rotate EN to TR

    :param e: East component
    :type e: np.ndarray
    :param n: North component
    :type n: np.ndarray
    :param baz: Back-azimuth
    :type baz: float
    :return: T and R components
    :rtype: tuple
    """
    angle = np.mod(baz+180, 360)
    r = n*cosd(angle) + e*sind(angle)
    t = e*cosd(angle) - n*sind(angle)
    return t, r
