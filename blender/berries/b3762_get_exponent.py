# get_exponent
#
# Copied verbatim from https://github.com/timpol/pysoplot
#   file src/pysoplot/misc.py, line 108
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_exponent(n):
    """Return order of magnitude of n
    """
    if n == 0:
        return 0. * n
    return int(np.floor(np.log10(abs(n))))
