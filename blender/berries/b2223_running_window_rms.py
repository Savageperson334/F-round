# running_window_rms
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/utility.py, line 1141
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def running_window_rms(data, window_size, mode="valid"):
    """
    Calculate the standard deviations of a running window over data.

    Parameters
    ----------
    data : :class:`numpy.ndarray` 1-d
        containing data to calculate stds from
    window_size : int
        sample size of running window
    mode : str
        see numpy.convolve for modes

    Returns
    -------
    :class:`numpy.ndarray` 1-d
        with stds, size data.size - window_size + 1
    """
    data2 = num.power(data, 2)
    window = num.ones(window_size) / float(window_size)
    return num.sqrt(num.convolve(data2, window, mode))
