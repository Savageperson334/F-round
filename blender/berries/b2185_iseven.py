# iseven
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/misc/math.py, line 25
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def iseven(x):
    """
    Test if integer(s) are even.

    Parameters
    ----------
    x : int OR list of int
        The integer(s) to test.

    Returns
    -------
    bool OR list of bool
        Whether or not ``x`` is even.
    """
    return (np.around(x).astype(int) & 0x1) == 0
