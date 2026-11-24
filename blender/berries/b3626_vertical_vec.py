# vertical_vec
#
# Copied verbatim from https://github.com/sphereman/ChemBlender_2_0
#   file _math.py, line 24
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


def normalize(vector):
    return vector/get_length(vector) if get_length(vector) else vector


def vertical_vec(pos1, pos2):
    v = normalize(pos2-pos1)
    if v[0] == 0 and v[1] == 0:
        vertical = np.array((1,0,0))
    else:
        vertical = normalize((-v[1], v[0], 0))
    return vertical
