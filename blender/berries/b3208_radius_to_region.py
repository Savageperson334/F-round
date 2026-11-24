# radius_to_region
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/orthodrome.py, line 1192
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

d2r = math.pi/180.

earthradius_equator = 6378.14 * 1000.

d2m = earthradius_equator*math.pi/180.

m2d = 1./d2m


def positive_region(region):
    '''
    Normalize parameterization of a rectangular geographical region.

    :param region: ``(west, east, south, north)`` in [deg].
    :type region: :py:class:`tuple` of :py:class:`float`

    :returns: ``(west, east, south, north)``, where ``west <= east`` and
        where ``west`` and ``east`` are in the range ``[-180., 180.+360.]``.
    :rtype: :py:class:`tuple` of :py:class:`float`
    '''
    west, east, south, north = [float(x) for x in region]

    assert -180. - 360. <= west < 180.
    assert -180. < east <= 180. + 360.
    assert -90. <= south < 90.
    assert -90. < north <= 90.

    if east < west:
        east += 360.

    if west < -180.:
        west += 360.
        east += 360.

    return (west, east, south, north)


def radius_to_region(lat, lon, radius):
    '''
    Get a rectangular region which fully contains a given circular region.

    :param lat: Latitude of the center point of circular region in [deg].
    :type lat: float
    :param lon: Longitude of the center point of circular region in [deg].
    :type lon: float
    :param radius: Radius of circular region in [m].
    :type radius: float

    :returns: Rectangular region as ``(east, west, south, north)`` in [deg] or
        ``None``.
    :rtype: tuple[float, float, float, float]
    '''
    radius_deg = radius * m2d
    if radius_deg < 45.:
        lat_min = max(-90., lat - radius_deg)
        lat_max = min(90., lat + radius_deg)
        absmaxlat = max(abs(lat_min), abs(lat_max))
        if absmaxlat > 89:
            lon_min = -180.
            lon_max = 180.
        else:
            lon_min = max(
                -180. - 360.,
                lon - radius_deg / math.cos(absmaxlat*d2r))
            lon_max = min(
                180. + 360.,
                lon + radius_deg / math.cos(absmaxlat*d2r))

        lon_min, lon_max, lat_min, lat_max = positive_region(
            (lon_min, lon_max, lat_min, lat_max))

        return lon_min, lon_max, lat_min, lat_max

    else:
        return None
