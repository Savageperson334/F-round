# quadraticEqn
#
# Copied verbatim from https://github.com/uafgeotools/array_processing
#   file array_processing/tools/array_characterization.py, line 375
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def quadraticEqn(a, b, c):
    r"""
    Roots of quadratic equation in the form :math:`ax^2 + bx + c = 0`.

    Args:
        a (int or float): Scalar coefficient of quadratic equation, can be
            complex
        b (int or float): Same as above
        c (int or float): Same as above

    Returns:
        list: Roots of quadratic equation in standard form

    See Also:
        :func:`numpy.roots` — Generic polynomial root finder

    Notes:
        Stable solutions, even for :math:`b^2 >> ac` or complex coefficients,
        per algorithm of Numerical Recipes 2nd ed., :math:`\S` 5.6.
    """

    # real coefficient branch
    if np.isreal([a, b, c]).all():
        # note np.sqrt(-1) = nan, so force complex argument
        if b:
            # std. sub-branch
            q = -0.5*(b + np.sign(b) * np.sqrt(complex(b * b - 4 * a * c)))
        else:
            # b = 0 sub-branch
            q = -np.sqrt(complex(-a * c))
    # complex coefficient branch
    else:
        if np.real(np.conj(b) * np.sqrt(b * b - 4 * a * c)) >= 0:
            q = -0.5*(b + np.sqrt(b * b - 4 * a * c))
        else:
            q = -0.5*(b - np.sqrt(b * b - 4 * a * c))
    # stable root solution
    x = [q/a, c/q]
    # parse real and/or int roots for tidy output
    for k in 0, 1:
        if np.real(x[k]) == x[k]:
            x[k] = float(np.real(x[k]))
            if int(x[k]) == x[k]:
                x[k] = int(x[k])
    return x
