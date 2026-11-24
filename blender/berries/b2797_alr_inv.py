# alr_inv
#
# Copied verbatim from https://github.com/morganjwilliams/exploratory-geochemistry
#   file src/EMimputation.py, line 30
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def alr_inv(X: np.ndarray, d:int = -1):
    m, n = X.shape
    X = np.c_[X, np.zeros(m)]
    X = np.exp(X)
    X = np.divide(X,  np.sum(X, axis=1)[:, np.newaxis]) # Closure

    if d < 0: d += X.shape[1]
    indexes = np.array([*range(0, X.shape[1])])
    indexes = [i for i in indexes[:-1] if i < d] + [-1] + [i for i in indexes[:-1] if i >= d]
    X = X[:, indexes]
    return X
