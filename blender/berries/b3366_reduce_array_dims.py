# reduce_array_dims
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/model/geometry.py, line 25
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def reduce_array_dims(array):
    '''
    Support function to reduce output array ndims from table
    '''

    if array.shape[0] == 1 and array.ndim > 1:
        return num.squeeze(array, axis=0)
    else:
        return array
