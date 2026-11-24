# biggest_common_divisor
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/utility.py, line 1291
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def biggest_common_divisor(a, b):
    """
    Find the biggest common divisor of two float numbers a and b.

    Parameters
    ----------
    a, b: float

    Returns
    -------
    int
    """

    while b > 0:
        rest = a % b
        a = b
        b = rest

    return int(a)
