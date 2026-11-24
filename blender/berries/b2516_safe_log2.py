# safe_log2
#
# Copied verbatim from https://github.com/kourgeorge/project-origin
#   file utils.py, line 79
#   licence (as GitHub reports it): BSD-2-Clause   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def safe_log2(number):
    if number <= np.e:
        return 0
    return int(number/10)
