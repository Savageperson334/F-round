# covmat_to_cormat
#
# Copied verbatim from https://github.com/timpol/pysoplot
#   file src/pysoplot/misc.py, line 65
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def covmat_to_cormat(cov):
    """
    Compute correlation matrix from covariance matrix. Based on:
    https://gist.github.com/wiso/ce2a9919ded228838703c1c7c7dad13b
    """
    v = np.sqrt(np.diag(cov))
    outer_v = np.outer(v, v)
    cor = cov / outer_v
    cor[cov == 0] = 0
    return cor
