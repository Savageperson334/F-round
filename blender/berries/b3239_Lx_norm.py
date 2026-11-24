# Lx_norm
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/trace.py, line 4042
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def Lx_norm(u, v, norm=2):
    '''
    Calculate the misfit denominator *m* and the normalization divisor *n*
    according to norm.

    The normalization divisor *n* is calculated from ``v``.

    :param u: :py:class:`numpy.ndarray`
    :param v: :py:class:`numpy.ndarray`
    :param norm: (default = 2)

    ``u`` and ``v`` must be of same size.
    '''

    if norm == 1:
        return (
            num.sum(num.abs(v-u)),
            num.sum(num.abs(v)))

    elif norm == 2:
        return (
            num.sqrt(num.sum((v-u)**2)),
            num.sqrt(num.sum(v**2)))

    else:
        return (
            num.power(num.sum(num.abs(num.power(v - u, norm))), 1./norm),
            num.power(num.sum(num.abs(num.power(v, norm))), 1./norm))
