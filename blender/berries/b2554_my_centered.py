# my_centered
#
# Copied verbatim from https://github.com/lermert/noisi
#   file noisi/util/windows.py, line 5
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def my_centered(arr, newsize):

    if newsize % 2 == 0:
        raise ValueError('Newsize must be odd.')

    # pad with zeros, if newsize > len(arr)
    newarr = np.zeros(newsize)

    # get the center portion of a 1-dimensional array correctly
    n = len(arr)
    i0 = (n - newsize) // 2
    if i0 < 0:
        i0 = (newsize - n) // 2
        newarr[i0: i0 + n] += arr

    else:
        if n % 2 == 0:
            # This is arbitrary
            # because the array has no 'center' sample
            i0 += 1
        newarr[:] += arr[i0: i0 + newsize]
    return newarr
