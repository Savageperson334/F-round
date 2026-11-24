# linear_dist_normalization
#
# Copied verbatim from https://github.com/kourgeorge/project-origin
#   file utils.py, line 93
#   licence (as GitHub reports it): BSD-2-Clause   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def linear_dist_normalization(p):
    p = np.asarray(p)
    p += abs(min(p))
    norm = sum(p)
    if norm == 0:
        norm = 1e-16
    res = p / norm
    return res
