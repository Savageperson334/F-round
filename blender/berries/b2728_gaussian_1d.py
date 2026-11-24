# gaussian_1d
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/src/utils/optimization.py, line 53
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def gaussian_1d(x_arr, xo, sigma, amplitude=1, offset=0):
    """"Return 1D gaussian function as array"""
    g = offset + amplitude * np.exp(- ((x_arr - float(xo)) ** 2) / (2 * sigma ** 2))
    return g.ravel()
