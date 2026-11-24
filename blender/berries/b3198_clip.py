# clip
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/orthodrome.py, line 86
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def clip(x, mi, ma):
    '''
    Clip values of an array.

    :param x: Continunous data to be clipped.
    :param mi: Clip minimum.
    :param ma: Clip maximum.
    :type x: :py:class:`numpy.ndarray`
    :type mi: float
    :type ma: float

    :return: Clipped data.
    :rtype: :py:class:`numpy.ndarray`
    '''
    return num.minimum(num.maximum(mi, x), ma)
