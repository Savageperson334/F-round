# distance_between_two_coordinates
#
# Copied verbatim from https://github.com/mnky9800n/Python-course-materials-for-seismology-students
#   file utilities/get_catalog_events.py, line 17
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def distance_between_two_coordinates(lat_a, lon_a, lat_b, lon_b):
    """
    calculates the distance between two LAT/LON coordinates

    accurate up to 200km distances

    returns single LON/LAT vector difference
    lat_a : float
    lon_a : float
    lat_b : float
    lon_b : float
    return : float
    """
    lat_diff = lat_a - lat_b
    lon_diff = lon_a - lon_b
    lat_km = 111.19 * lat_diff

    lat_radians = np.deg2rad(lat_a)
    lon_km = 111.19 * lon_diff * np.cos(lat_radians)
    distance = np.array([lon_km, lat_km])
    x, y = distance
    return np.sqrt(x**2 + y**2)
