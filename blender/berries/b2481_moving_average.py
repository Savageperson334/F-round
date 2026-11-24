# moving_average
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 926
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def moving_average(data, window):

    weights = np.repeat(1.0, window)/window
    smas = np.convolve(data, weights, 'valid')

    print (smas)
    print (data[:int(window/2)])

    return list(data[:int(window/2)]) + list(smas) + list(data[-int(window/2):-1])
