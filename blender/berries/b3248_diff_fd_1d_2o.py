# diff_fd_1d_2o
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/util.py, line 1028
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def diff_fd_1d_2o(dt, data):
    '''
    Approximate first derivative of an array (second order, central FD).

    :param dt: sampling interval
    :param data: NumPy array with data samples

    :returns: NumPy array with same shape as input

    Interior points are approximated to second order, edge points to first
    order right- or left-sided respectively.

    Uses :py:func:`numpy.gradient`.
    '''

    return num.gradient(data, dt)
