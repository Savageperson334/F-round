# power
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/util/util.py, line 305
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#   the same function also appears in: agilescientific/in-bruges
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def power(start, stop, num):
    """
    Nonlinear space following a power function.
    """
    x = np.linspace(0, 8, num)
    y = 1 - 2**-x
    return min(start, stop) + abs(stop-start) * y
