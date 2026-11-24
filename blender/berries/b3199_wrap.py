# wrap
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/orthodrome.py, line 103
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def wrap(x, mi, ma):
    '''
    Wrapping continuous data to fundamental phase values.

    .. math::
        x_{\\mathrm{wrapped}} = x_{\\mathrm{cont},i} -
            \\frac{ x_{\\mathrm{cont},i} - r_{\\mathrm{min}} }
                  { r_{\\mathrm{max}} -  r_{\\mathrm{min}}}
            \\cdot ( r_{\\mathrm{max}} -  r_{\\mathrm{min}}),\\quad
        x_{\\mathrm{wrapped}}\\; \\in
            \\;[ r_{\\mathrm{min}},\\, r_{\\mathrm{max}}].

    :param x: Continunous data to be wrapped.
    :param mi: Minimum value of wrapped data.
    :param ma: Maximum value of wrapped data.
    :type x: :py:class:`numpy.ndarray`
    :type mi: float
    :type ma: float

    :return: Wrapped data.
    :rtype: :py:class:`numpy.ndarray`
    '''
    return x - num.floor((x-mi)/(ma-mi)) * (ma-mi)
