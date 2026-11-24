# linreg
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 894
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def linreg(x, y):
    '''
    Linear regression: returns the offset a and slope b for the function y_lin(x) = a + b*x
    that approximates the distribtion y(x) the best (sum of squares of residuals is minimized).

    input:
        x: array-like, values where y-values are valid
        y: array-like, must have same length as x, values y(x)

    output:
        a = offset of linear function resulting from regression
        b = slope of linear function resulting from regression
    '''
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b = SS_xy / SS_xx  # slope
    a = m_y - b * m_x  # zero-offset

    return(a, b)
