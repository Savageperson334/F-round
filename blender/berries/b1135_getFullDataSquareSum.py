# getFullDataSquareSum
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/dataprocessing.py, line 170
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def getFullDataSquareSum(data):
    sums = np.zeros_like(data)

    sums[:len(data)-1, :len(data[0]) - 1] += data[1:, 1:]
    sums[:len(data)-1, :] += data[1:, :]
    sums[:len(data)-1, 1:] += data[1:, :len(data[0]) - 1]

    sums[:, :len(data[0]) - 1] += data[:, 1:]
    sums += data
    sums[:, 1:] += data[:, :len(data[0]) - 1]

    sums[1:, :len(data[0]) - 1] += data[:len(data) - 1, 1:]
    sums[1:, :] += data[:len(data) - 1, :]
    sums[1:, 1:] += data[:len(data) - 1, :len(data[0]) - 1]

    return sums
