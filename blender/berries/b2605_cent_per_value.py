# cent_per_value
#
# Copied verbatim from https://github.com/lockepatton/sonipy
#   file sonipy/scales/frequency.py, line 11
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cent_per_value(f_min, f_max, v_min, v_max):
    """
    This function takes in a frequency max and min, and y value max and min and returns a y scale parameter in units of cents/y value.
    Cents are a logarithmic unit of tone intervals (https://en.wikipedia.org/wiki/Cent_(music)).

    Parameters
    ----------
    f_min : float
        Minimum frequency.
    f_max : float
        Maximum frequency.
    v_min : float
        Minimum y value.
    v_max : float
        Maximum y value.

    Returns
    -------
    float
        A y-scale parameter in units of cents/y value.

    """
    step = 1200 * np.log2(f_max / f_min) / (v_max - v_min)
    return step
