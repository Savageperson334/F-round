# from_min_ms
#
# Copied verbatim from https://github.com/lockepatton/sonipy
#   file sonipy/scales/durations.py, line 32
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def from_min_ms(x, dtime_min):
    """
    Calculates a time scale in units of x value / time (ms), by matching the smallest time step in the x array to the input dtime_min.

    Parameters
    ----------
    x : arr
        Array of x positions that will correspond to blip times.
    dtime_min : float
        Minimum allowed time difference between blips (in ms).

    Returns
    -------
    float
        Returns a time scale calculated from the minimum dt.

    """
    dx = np.subtract(x[1:], x[0:-1])
    dx_min = np.min(dx[np.nonzero(dx)])  # min(dt)
    scale = float(dx_min) / float(dtime_min)  # x value / ms
    return scale
