# find_nearest
#
# Copied verbatim from https://github.com/adjtomo/pysep
#   file pysep/pplot.py, line 414
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def find_nearest(array, value):
    """
    Find the nearest index in a consecutive (time) array given a chosen value
    """
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx
