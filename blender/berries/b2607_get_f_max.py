# get_f_max
#
# Copied verbatim from https://github.com/lockepatton/sonipy
#   file sonipy/scales/frequency.py, line 63
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_f_max(f_min, cents_per_value, v_min, v_max):
    """
    This function takes in a y value max and min, a minimum frequency and a y scale parameter in units of cents/y value, and returns the maximum frequency that fits to such a scale.
    Cents are a logarithmic unit of tone intervals (https://en.wikipedia.org/wiki/Cent_(music)).

    Parameters
    ----------
    f_min : float
        Minimum frequency.
    cents_per_value : float
        A y scale parameter in units of cents/y value.
    v_min : float
        Minimum y value.
    v_max : float
        Maximum y value.

    Returns
    -------
    float
        Maximum frequency.

    """
    f_max = f_min * (2 ** ((v_max - v_min) * cents_per_value / 1200))
    return f_max
