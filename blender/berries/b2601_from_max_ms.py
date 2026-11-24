# from_max_ms
#
# Copied verbatim from https://github.com/lockepatton/sonipy
#   file sonipy/scales/durations.py, line 9
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def from_max_ms(x, dtime_max):
    """
    Calculates a time scale in units of x value / time (ms), by matching the largest time step in the x array to the input dtime_max.

    Parameters
    ----------
    x : arr
        Array of x positions that will correspond to blip times.
    dtime_max : float
        Maximum allowed time difference between blips (in ms).

    Returns
    -------
    float
        Returns a time scale calculated from the maximum dt.

    """
    dx = np.subtract(x[1:], x[0:-1])
    dx_max = max(dx)
    scale = float(dx_max) / float(dtime_max)  # x value / ms
    return scale
