# inv_clr
#
# Copied verbatim from https://github.com/morganjwilliams/exploratory-geochemistry
#   file src/compositions.py, line 219
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def inv_clr(Y: np.ndarray):
    X = np.exp(Y)  # Inverse of log operation
    X = np.divide(X, np.nansum(X, axis=1)[:, np.newaxis])  #Closure operation
    return X
