# gaussian
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file fatiando/utils.py, line 508
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy


def gaussian(x, mean, std):
    """
    Non-normalized Gaussian function

    .. math::

        G(x,\\bar{x},\sigma) = \exp\\left(-\\frac{(x-\\bar{x})^2}{\sigma^2}
        \\right)

    Parameters:

    * x : float or array
        Values at which to calculate the Gaussian function
    * mean : float
        The mean of the distribution :math:`\\bar{x}`
    * std : float
        The standard deviation of the distribution :math:`\sigma`

    Returns:

    * gauss : array
        Gaussian function evaluated at *x*

    """
    return numpy.exp(-1 * ((mean - x) / std) ** 2)
