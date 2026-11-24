# from_total_ms
#
# Copied verbatim from https://github.com/lockepatton/sonipy
#   file sonipy/scales/durations.py, line 55
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def from_total_ms(x, time_total):
    """
    Calculates a time scale in units of x value / time (ms), by matching the total length of x array to the input time_total.

    Parameters
    ----------
    x : arr
        Array of x positions that will correspond to blip times.
    time_total : float
        Total time difference between first and last blip (in ms).

    Returns
    -------
    float
        Returns a time scale calculated from the total dt.

    """
    dx_total = abs(x[0] - x[-1])
    scale = float(dx_total) / float(time_total) # x value / ms
    return scale
