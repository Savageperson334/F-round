# slim
#
# Copied verbatim from https://github.com/timpol/pysoplot
#   file src/pysoplot/regression.py, line 660
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def slim(n):
    """Upper bound of 95% confidence interval on s (spine width) for Spine
    linear regression algorithm. Derived from simulation of Gaussian distributed
    datasets. See Powell et al., (2020).

    References
    ----------
    Powell, R., Green, E.C.R., Marillo Sialer, E., Woodhead, J., 2020. Robust
    isochron calculation. Geochronology 2, 325–342.
    https://doi.org/10.5194/gchron-2-325-2020

    """
    return 1.92 - 0.162 * np.log(10 + n)
