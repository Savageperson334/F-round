# nmad
#
# Copied verbatim from https://github.com/timpol/pysoplot
#   file src/pysoplot/stats.py, line 10
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def nmad(x):
    """
    Median absolute deviation about the median (MAD) normalised such that
    statistic will be equal to the standard deviation for a standard normal
    random variable.
    """
    return 1.4826 * np.median(np.absolute(x - np.median(x)))
