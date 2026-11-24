# gaisser_hillas
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 692
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def gaisser_hillas(X, xmax, X0, lam, nmax=1):
    """ returns the Gaisser-Hillers function
        Reference: http://en.wikipedia.org/wiki/Gaisser%E2%80%93Hillas_function
    """
    return nmax * ((X - X0) / (xmax - X0)) ** ((xmax - X0) / lam) * np.exp((xmax - X) / lam)
