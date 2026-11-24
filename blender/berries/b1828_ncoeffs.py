# ncoeffs
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file fatiando/gravmag/eqlayer.py, line 264
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ncoeffs(degree):
    """
    Calculate the number of coefficients in a bivarite polynomail.

    Parameters:

    * degree : int
        The degree of the polynomial

    Returns:

    * n : int
        The number of coefficients

    Examples:

    >>> ncoeffs(1)
    3
    >>> ncoeffs(2)
    6
    >>> ncoeffs(3)
    10
    >>> ncoeffs(4)
    15

    """
    return sum(range(1, degree + 2))
