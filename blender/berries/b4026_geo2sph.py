# geo2sph
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 416
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def geo2sph(dep, lat, lon):
    """Convert geographic coordinates to spherical coordinates.

    :param dep: Depth from surface
    :type dep: float or np.ndarray
    :param lat: Latitude
    :type lat: float or np.ndarray
    :param lon: Longitude
    :type lon: float or np.ndarray
    :return: spherical coordinate r, theta, phi
    :rtype: list
    """
    theta = np.radians(90. - lat)
    phi = np.radians(lon)
    r = 6371 - dep
    return r, theta, phi
