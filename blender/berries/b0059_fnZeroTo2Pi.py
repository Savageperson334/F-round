# fnZeroTo2Pi
#
# Copied verbatim from https://github.com/AshivDhondea/Satellite_Ground_Track_Plotting_Python
#   file AstroFunctions.py, line 43
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def fnZeroTo2Pi(rotangle):
    """
    Wraps angle to fit in [0,2pi).
    Works in [rad] not [deg]
    Date: 7 October 2016
    """
    wrappedangle = rotangle % (2*math.pi);
    return wrappedangle
