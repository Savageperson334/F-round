# unit
#
# Copied verbatim from https://github.com/meng-yijie1996/LBM-Ferrofluid
#   file renderutils/dibr/utils/perspective.py, line 24
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ferrofluids and magnetic materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def unit(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm
