# extend_1d_coordinate_array
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file examples/automap_example2.py, line 44
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def extend_1d_coordinate_array(array):
    '''
    Extend 1D coordinate array for gridded data, that grid corners are plotted
    right
    '''
    dx = array[1] - array[0]

    out = num.zeros(array.shape[0] + 2)
    out[1:-1] = array.copy()
    out[0] = array[0] - dx / 2.
    out[-1] = array[-1] + dx / 2.

    return out
