# dB_to_linear
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 29
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def dB_to_linear(dB):
    """ conversion from decibel scale to linear scale

    Parameters
    ------------
    dB : float
        quantity in dB units

    Returns
    --------
    linear : float
        quantity in linear units
    """
    return 10 ** (dB / 10.)
