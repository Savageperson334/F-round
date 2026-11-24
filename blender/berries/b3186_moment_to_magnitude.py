# moment_to_magnitude
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/moment_tensor.py, line 224
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def moment_to_magnitude(moment):
    '''
    Convert scalar moment to moment magnitude Mw.

    :param moment: scalar moment [Nm]
    :returns: moment magnitude Mw

    Moment magnitude is defined as

    .. math::

        M_\\mathrm{w} = {\\frac{2}{3}}\\log_{10}(M_0 \\cdot 10^7) - 10.7

    where :math:`M_0` is the scalar moment given in [Nm].

    .. note::

        Global CMT uses 10.7333333 instead of 10.7, based on [Kanamori 1977],
        10.7 is from [Hanks and Kanamori 1979].
    '''

    return num.log10(moment*1.0e7) / 1.5 - 10.7
