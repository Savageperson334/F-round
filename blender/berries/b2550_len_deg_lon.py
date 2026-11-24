# len_deg_lon
#
# Copied verbatim from https://github.com/lermert/noisi
#   file noisi/util/geo.py, line 77
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import cos
from math import pi
from math import sin
from math import sqrt


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


def len_deg_lon(lat):
    (a, b, e_2, f) = wgs84()

    # This is the length of one degree of longitude
    # approx. after WGS84, at latitude lat
    # in m
    lat = pi / 180 * lat
    dlon = (pi * a * cos(lat)) / 180 * sqrt((1 - e_2 * sin(lat) ** 2))
    return round(dlon, 5)
