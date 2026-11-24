# gaisser_hillas1_parametric
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 683
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def gaisser_hillas1_parametric(x, xmax, nmax=1):
    """ return one parametric form of Gaisser-Hillers function
        Reference: http://en.wikipedia.org/wiki/Gaisser%E2%80%93Hillas_function and
        Darko Veberic (2012). "Lambert W Function for Applications in Physics".
        Computer Physics Communications 183 (12): 2622–2628. arXiv:1209.0735. doi:10.1016/j.cpc.2012.07.008.
    """
    return nmax * (x / xmax) ** xmax * np.exp(xmax - x)
