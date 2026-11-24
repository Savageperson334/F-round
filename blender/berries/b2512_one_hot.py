# one_hot
#
# Copied verbatim from https://github.com/kourgeorge/project-origin
#   file utils.py, line 40
#   licence (as GitHub reports it): BSD-2-Clause   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def one_hot(arg, size):
    result = np.zeros(size)
    if 0 <= arg < size:
        result[arg] = 1
        return result
    else:
        return None
