# nearest
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/util/util.py, line 165
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def nearest(a, num):
    """
    Finds the array's nearest value to a given num.

    Args:
        a (ndarray): An array.
        num (float): The value to find the nearest to.

    Returns:
        float. The normalized array.
    """
    a = np.array(a, dtype=float)
    return a.flat[np.abs(a - num).argmin()]
