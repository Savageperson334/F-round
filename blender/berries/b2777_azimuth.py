# azimuth
#
# Copied verbatim from https://github.com/mnky9800n/Python-course-materials-for-seismology-students
#   file utilities/distance.py, line 31
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def _prepare_coords(lons1, lats1, lons2, lats2):
    """
    Convert two pairs of spherical coordinates in decimal degrees
    to numpy arrays of radians. Makes sure that respective coordinates
    in pairs have the same shape.
    """
    lons1 = np.radians(lons1)
    lats1 = np.radians(lats1)
    assert lons1.shape == lats1.shape
    lons2 = np.radians(lons2)
    lats2 = np.radians(lats2)
    assert lons2.shape == lats2.shape
    return lons1, lats1, lons2, lats2


def azimuth(lons1, lats1, lons2, lats2):
    """
    Calculate the azimuth between two points or two collections of points.
    Parameters are the same as for :func:`geodetic_distance`.
    Implements an "alternative formula" from
    http://williams.best.vwh.net/avform.htm#Crs
    :returns:
        Azimuth as an angle between direction to north from first point and
        direction to the second point measured clockwise in decimal degrees.
    """
    lons1, lats1, lons2, lats2 = _prepare_coords(lons1, lats1, lons2, lats2)
    cos_lat2 = np.cos(lats2)
    true_course = np.degrees(np.arctan2(
        np.sin(lons1 - lons2) * cos_lat2,
        np.cos(lats1) * np.sin(lats2)
        - np.sin(lats1) * cos_lat2 * np.cos(lons1 - lons2)
    ))
    return (360 - true_course) % 360
