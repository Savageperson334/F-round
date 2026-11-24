# geodetic_to_ecef
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/orthodrome.py, line 1296
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num

earth_oblateness = 1./298.257223563

earthradius_equator = 6378.14 * 1000.


def geodetic_to_ecef(lat, lon, alt):
    '''
    Convert geodetic coordinates to Earth-Centered, Earth-Fixed (ECEF)
    Cartesian coordinates. [#1]_ [#2]_

    :param lat: Geodetic latitude in [deg].
    :param lon: Geodetic longitude in [deg].
    :param alt: Geodetic altitude (height) in [m] (positive for points outside
       the geoid).
    :type lat: float
    :type lon: float
    :type alt: float

    :return: ECEF Cartesian coordinates (X, Y, Z) in [m].
    :rtype: tuple[float, float, float]

    .. [#1] https://en.wikipedia.org/wiki/ECEF
    .. [#2] https://en.wikipedia.org/wiki/Geographic_coordinate_conversion
       #From_geodetic_to_ECEF_coordinates
    '''

    f = earth_oblateness
    a = earthradius_equator
    e2 = 2*f - f**2

    lat, lon = num.radians(lat), num.radians(lon)
    # Normal (plumb line)
    N = a / num.sqrt(1.0 - (e2 * num.sin(lat)**2))

    X = (N+alt) * num.cos(lat) * num.cos(lon)
    Y = (N+alt) * num.cos(lat) * num.sin(lon)
    Z = (N*(1.0-e2) + alt) * num.sin(lat)

    return (X, Y, Z)
