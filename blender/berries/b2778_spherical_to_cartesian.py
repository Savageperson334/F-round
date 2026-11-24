# spherical_to_cartesian
#
# Copied verbatim from https://github.com/mnky9800n/Python-course-materials-for-seismology-students
#   file utilities/distance.py, line 98
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

EARTH_RADIUS = 6371.0


def spherical_to_cartesian(lons, lats, depths):
    """
    Return the position vectors (in Cartesian coordinates) of list of spherical
    coordinates.

    For equations see: http://mathworld.wolfram.com/SphericalCoordinates.html.

    Parameters are components of spherical coordinates in a form of scalars,
    lists or numpy arrays. ``depths`` can be ``None`` in which case it's
    considered zero for all points.

    :returns:
        ``numpy.array`` of 3d vectors representing points' coordinates in
        Cartesian space. The array has the same shape as parameter arrays.
        In particular it means that if ``lons`` and ``lats`` are scalars,
        the result is a single 3d vector. Vector of length ``1`` represents
        distance of 1 km.

    See also :func:`cartesian_to_spherical`.
    """
    phi = np.radians(lons)
    theta = np.radians(lats)
    if depths is None:
        rr = EARTH_RADIUS
    else:
        rr = EARTH_RADIUS - np.array(depths)
    cos_theta_r = rr * np.cos(theta)
    xx = cos_theta_r * np.cos(phi)
    yy = cos_theta_r * np.sin(phi)
    zz = rr * np.sin(theta)
    vectors = np.array([xx.transpose(), yy.transpose(), zz.transpose()]) \
        .transpose()
    return vectors
