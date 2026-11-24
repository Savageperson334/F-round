# linear
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/holography/analysis/fitfunctions.py, line 10
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def linear(x, m, b):
    r"""
    For fitting a line.

    .. math:: y(x) = mx + b

    Parameters
    ----------
    x : numpy.ndarray
        Some independent variable.
    m : float
        Slope of the line.
    b : float
        :math:`y`-intercept of the line.

    Returns
    -------
    y : numpy.ndarray
        Line evaluated at all ``x``.
    """
    return m * x + b
