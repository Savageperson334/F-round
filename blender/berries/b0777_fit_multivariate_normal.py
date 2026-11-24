# fit_multivariate_normal
#
# Copied verbatim from https://github.com/XiaokangLiuCUG/DeepMorph
#   file Triassic results and codes/recovery simulations.py, line 50
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Laboratories, geochemistry, chemistry and microscopes
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def fit_multivariate_normal(coordinates):
    mean_est = np.mean(coordinates, axis=0)
    cov_est = np.cov(coordinates, rowvar=False)
    return mean_est, cov_est
