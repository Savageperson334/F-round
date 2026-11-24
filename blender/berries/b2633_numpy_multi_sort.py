# numpy_multi_sort
#
# Copied verbatim from https://github.com/mapleee/dvs-sonification
#   file utils/event_process.py, line 98
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def numpy_multi_sort(array):
    value = [tuple(a) for a in array]
    dtyp = [('x', int), ('y', int)]
    array = np.array(value, dtype=dtyp)
    sorted_arr = np.sort(array, order=['x', 'y'])
    sorted_arr = np.array([list(a) for a in sorted_arr])
    return sorted_arr
