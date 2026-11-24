# gaussian2d
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file fatiando/utils.py, line 535
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy


def gaussian2d(x, y, sigma_x, sigma_y, x0=0, y0=0, angle=0.0):
    """
    Non-normalized 2D Gaussian function

    Parameters:

    * x, y : float or arrays
        Coordinates at which to calculate the Gaussian function
    * sigma_x, sigma_y : float
        Standard deviation in the x and y directions
    * x0, y0 : float
        Coordinates of the center of the distribution
    * angle : float
        Rotation angle of the gaussian measure from the x axis (north) growing
        positive to the east (positive y axis)

    Returns:

    * gauss : array
        Gaussian function evaluated at *x*, *y*

    """
    theta = -1 * angle * numpy.pi / 180.
    tmpx = 1. / sigma_x ** 2
    tmpy = 1. / sigma_y ** 2
    sintheta = numpy.sin(theta)
    costheta = numpy.cos(theta)
    a = tmpx * costheta + tmpy * sintheta ** 2
    b = (tmpy - tmpx) * costheta * sintheta
    c = tmpx * sintheta ** 2 + tmpy * costheta ** 2
    xhat = x - x0
    yhat = y - y0
    return numpy.exp(-(a * xhat ** 2 + 2. * b * xhat * yhat + c * yhat ** 2))
