# round_down
#
# Copied verbatim from https://github.com/timpol/pysoplot
#   file src/pysoplot/misc.py, line 128
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def round_down(n, sf=2):
    """ Round float down to n significant figures.
    """
    if n == 0:
        return 0. * n   # for array inputs
    return round(n, sf - int(np.floor(np.log10(abs(n)))) - 1)
