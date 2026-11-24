# zernike_order_number
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/holography/toolbox/phase/_zernike.py, line 90
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def zernike_order_number(radial_order):
    """
    Get the number of Zernike polynomials under (inclusive) a given radial order.

    For radial order :math:`n`, this evaluates to :math:`(n+1)(n+2)/2`.

    Parameters
    ----------
    radial_order : int
        Maximum radial order to include.

    Returns
    -------
    count : int
        Number of Zernike polynomials through this radial order, one past the largest
        ANSI index.
    """
    return (radial_order + 1) * (radial_order + 2) // 2
