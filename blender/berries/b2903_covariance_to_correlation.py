# covariance_to_correlation
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 882
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def covariance_to_correlation(M):
    """ converts covariance matrix into correlation matrix
    """
    D = np.diagflat(np.diag(M)) ** 0.5
    Dinv = np.linalg.inv(D)
    return np.dot(Dinv, np.dot(M, Dinv))
