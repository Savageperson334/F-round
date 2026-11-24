# numpy_correlate_emulate
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/trace.py, line 3540
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def numpy_correlate_lag_range(a, b, mode='valid', use_fft=False):
    '''
    Get range of lags for which :py:func:`numpy.correlate` produces values.
    '''

    a = num.asarray(a)
    b = num.asarray(b)

    kmin = -(b.size-1)
    if mode == 'full':
        klen = a.size-kmin
    elif mode == 'same':
        klen = max(a.size, b.size)
        kmin += (a.size+b.size-1 - max(a.size, b.size)) // 2 + \
            int(not use_fft and a.size % 2 == 0 and b.size > a.size)
    elif mode == 'valid':
        klen = abs(a.size - b.size) + 1
        kmin += min(a.size, b.size) - 1

    return kmin, kmin + klen - 1


def numpy_correlate_emulate(a, b, mode='valid'):
    '''
    Slow version of :py:func:`numpy.correlate` for comparison.
    '''

    a = num.asarray(a)
    b = num.asarray(b)
    kmin = -(b.size-1)
    klen = a.size-kmin
    kmin, kmax = numpy_correlate_lag_range(a, b, mode=mode)
    kmin = int(kmin)
    kmax = int(kmax)
    klen = kmax - kmin + 1
    c = num.zeros(klen, dtype=num.promote_types(b.dtype, a.dtype))
    for k in range(kmin, kmin+klen):
        imin = max(0, -k)
        ilen = min(b.size, a.size-k) - imin
        c[k-kmin] = num.sum(
            a[imin+k:imin+ilen+k] * num.conj(b[imin:imin+ilen]))

    return c
