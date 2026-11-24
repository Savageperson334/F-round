# cosdelta_numpy
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/orthodrome.py, line 188
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num
import math

d2r = math.pi/180.


def cosdelta_numpy(a_lats, a_lons, b_lats, b_lons):
    '''
    Cosine of the angular distance between two points ``a`` and ``b`` on a
    sphere.

    This function returns the cosines of the distance
    angles *delta* between two points ``a`` and ``b`` given as
    :py:class:`numpy.ndarray`.
    The coordinates are expected to be given in geographical coordinates
    and in degrees. For numerical stability a maximum of ``1.0`` is enforced.

    Please find the details of the implementation in the documentation of
    the function :py:func:`pyrocko.orthodrome.cosdelta` above.

    :param a_lats: Latitudes in [deg] point A.
    :param a_lons: Longitudes in [deg] point A.
    :param b_lats: Latitudes in [deg] point B.
    :param b_lons: Longitudes in [deg] point B.
    :type a_lats: :py:class:`numpy.ndarray`
    :type a_lons: :py:class:`numpy.ndarray`
    :type b_lats: :py:class:`numpy.ndarray`
    :type b_lons: :py:class:`numpy.ndarray`

    :return: Cosdelta.
    :type b_lons: :py:class:`numpy.ndarray`, ``(N)``
    '''
    return num.minimum(
        1.0,
        num.sin(a_lats*d2r) * num.sin(b_lats*d2r) +
        num.cos(a_lats*d2r) * num.cos(b_lats*d2r) *
        num.cos(d2r*(b_lons-a_lons)))
