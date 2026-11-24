# get_length
#
# Copied verbatim from https://github.com/sphereman/ChemBlender_2_0
#   file _math.py, line 5
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_length(vector):
    length = np.linalg.norm(vector)
    return length
