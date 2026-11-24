# pos_def
#
# Copied verbatim from https://github.com/timpol/pysoplot
#   file src/pysoplot/misc.py, line 28
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def pos_def(x, tol=1e-8):
    """
    Verify that matrix is positive semi-definite.
    Based on numpy multivariate_normal code, e.g.:
    https://github.com/numpy/numpy/blob/main/numpy/random/mtrand.pyx
    """
    x = np.asarray(x, dtype=np.double)
    (u, s, v) = np.linalg.svd(x)
    psd = np.allclose(np.dot(v.T * s, v), x, rtol=tol, atol=tol)
    return psd
