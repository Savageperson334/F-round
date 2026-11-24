# nancov
#
# Copied verbatim from https://github.com/morganjwilliams/exploratory-geochemistry
#   file src/compositions.py, line 14
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def nancov(X, method='replace'):
    """
    Generates a covariance matrix excluding nan-components.
    Done on a column-column/pairwise basis.
    The result Y may not be a positive definite matrix.
    """
    if method=='rowexclude':
        Xnanfree = X[np.all(np.isfinite(X), axis=1), :].T
        #assert Xnanfree.shape[1] > Xnanfree.shape[0]
        #(1/m)X^T*X
        return np.cov(Xnanfree)
    else:
        X = np.array(X, ndmin=2, dtype=float)
        X -= np.nanmean(X, axis=0)#[:, np.newaxis]
        cov = np.empty((X.shape[1], X.shape[1]))
        cols = range(X.shape[1])
        for n in cols:
            for m in [i for i in cols if i>=n] :
                fn = np.isfinite(X[:, n])
                fm = np.isfinite(X[:, m])
                if method=='replace':
                    X[~fn, n] = 0
                    X[~fm, m] = 0
                    fact = fn.shape[0] - 1
                    c= np.dot(X[:, n], X[:, m])/fact
                else:
                    f = fn & fm
                    fact = f.shape[0] - 1
                    c = np.dot(X[f, n], X[f, m])/fact
                cov[n, m] = c
                cov[m, n] = c
        return cov
