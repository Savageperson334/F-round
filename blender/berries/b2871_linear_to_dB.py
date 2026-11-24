# linear_to_dB
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 13
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def linear_to_dB(linear):
    """ conversion to decibel scale

    Parameters
    ------------
    linear : float
        quantity in linear units

    Returns
    --------
    dB : float
        quantity in dB units
    """
    return 10 * np.log10(linear)
