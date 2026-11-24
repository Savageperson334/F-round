# root
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/util/util.py, line 296
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#   the same function also appears in: agilescientific/in-bruges
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def root(start, stop, num):
    """
    Nonlinear space following a sqrt function.
    """
    x = np.linspace(0, 1, num)
    y = np.sqrt(x)
    return min(start, stop) + abs(stop-start) * y
