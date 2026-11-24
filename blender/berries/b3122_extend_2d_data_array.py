# extend_2d_data_array
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file examples/automap_example2.py, line 59
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def extend_2d_data_array(array):
    '''
    Extend 2D data array for gridded data, that grid corners are plotted
    right
    '''
    out = num.zeros((array.shape[0] + 2, array.shape[1] + 2))
    out[1:-1, 1:-1] = array
    out[1:-1, 0] = array[:, 0]
    out[1:-1, -1] = array[:, -1]
    out[0, 1:-1] = array[0, :]
    out[-1, 1:-1] = array[-1, :]

    for i, j in zip([-1, -1, 0, 0], [-1, 0, -1, 0]):
        out[i, j] = array[i, j]

    return out
