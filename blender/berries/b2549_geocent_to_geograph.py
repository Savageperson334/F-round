# geocent_to_geograph
#
# Copied verbatim from https://github.com/lermert/noisi
#   file noisi/util/geo.py, line 70
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def wgs84():

    # semi-major axis, in m
    a = 6378137.0

    # semi-minor axis, in m
    b = 6356752.314245

    # inverse flattening f
    f = a / (a - b)

    # squared eccentricity e
    e_2 = (a ** 2 - b ** 2) / a ** 2

    return(a, b, e_2, f)


def geocent_to_geograph(theta):
    # the other way around
    e2 = wgs84()[2]
    theta = np.rad2deg(np.arctan(np.tan(np.deg2rad(theta)) / (1 - e2)))
    return(theta)
