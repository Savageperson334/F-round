# inverse_additive_log_ratio
#
# Copied verbatim from https://github.com/morganjwilliams/exploratory-geochemistry
#   file src/compositions.py, line 167
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def close(X: np.ndarray):
    if X.ndim == 2:
        return np.divide(X, np.sum(X, axis=1)[:, np.newaxis])
    else:
        return np.divide(X, np.sum(X, axis=0))


def inverse_additive_log_ratio(Y: np.ndarray, ind=-1):
    """
    Inverse additive log ratio transform.
    """
    assert Y.ndim in [1, 2]

    X = Y.copy()
    dimensions = X.shape[X.ndim-1]
    idx = np.arange(0, dimensions+1)

    if ind != -1:
        idx = np.array(list(idx[idx < ind]) + 
                       [-1] + 
                       list(idx[idx >= ind+1]-1))

    # Add a zero-column and reorder columns
    if Y.ndim == 2:
        X = np.concatenate((X, np.zeros((X.shape[0], 1))), axis=1)
        X = X[:, idx]
    else:
        X = np.append(X, np.array([0]))
        X = X[idx]

    # Inverse log and closure operations
    X = np.exp(X)
    X = close(X)
    return X
