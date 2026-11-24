# emptynanmean
#
# Copied verbatim from https://github.com/kourgeorge/project-origin
#   file utils.py, line 73
#   licence (as GitHub reports it): BSD-2-Clause   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def emptynanmean(array):
    if array is not None and len(array) > 0:
        return np.nanmean(array)
    return 0
