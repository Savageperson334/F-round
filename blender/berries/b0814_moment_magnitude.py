# moment_magnitude
#
# Copied verbatim from https://github.com/adjtomo/pysep
#   file pysep/utils/mt.py, line 38
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def moment_magnitude(moment, c=10.7):
    """
    Return the moment magitude, M_w, based on a seismic moment. Equation from
    Hanks & Kanamori (1979)

    :type c: float
    :param c: correction factor for conversion, 10.7 for units of N*m,
        16.1 for units of dyne*cm
    :type moment: float
    :param moment: the seismic moment, in units of N*m
    :rtype: float
    :return: moment magnitude, M_w
    """
    return 2 / 3 * np.log10(moment) - c
