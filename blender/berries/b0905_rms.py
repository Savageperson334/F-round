# rms
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/util/util.py, line 91
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rms(a, axis=None):
    """
    Calculates the RMS of an array.

    Args:
        a (ndarray). A sequence of numbers to apply the RMS to.
        axis (int). The axis along which to compute. If not given or None,
            the RMS for the whole array is computed.

    Returns:
        ndarray: The RMS of the array along the desired axis or axes.
    """
    a = np.array(a)
    if axis is None:
        div = a.size
    else:
        div = a.shape[axis]
    ms = np.sum(a**2.0, axis=axis) / div
    return np.sqrt(ms)
