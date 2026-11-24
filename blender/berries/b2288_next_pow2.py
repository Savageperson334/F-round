# next_pow2
#
# Copied verbatim from https://github.com/interactive-sonification/pya
#   file pya/helper/helpers.py, line 189
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def next_pow2(x):
    """Find the closest pow of 2 that is great or equal or x, 
    based on shift_bit_length

    Parameters
    ----------
    x : int
        A positive number

    Returns
    -------
    _ : int
        The cloest  integer that is greater or equal to input x.
    """
    if x < 0:
        raise AttributeError("x needs to be positive integer.")
    return 1 << (x - 1).bit_length()
