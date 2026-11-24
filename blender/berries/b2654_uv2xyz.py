# uv2xyz
#
# Copied verbatim from https://github.com/matsuren/crownconv360depth
#   file dataloader/icosahedron_dataset.py, line 139
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def uv2xyz(uv):
    sin_u = np.sin(uv[..., 0])
    cos_u = np.cos(uv[..., 0])
    sin_v = np.sin(uv[..., 1])
    cos_v = np.cos(uv[..., 1])
    return np.stack([
        cos_v * sin_u,
        sin_v,
        cos_v * cos_u,
    ], axis=-1)
