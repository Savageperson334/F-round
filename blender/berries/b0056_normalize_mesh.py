# normalize_mesh
#
# Copied verbatim from https://github.com/AronKovacs/mesh-texture-synthesis
#   file style_transfer.py, line 207
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Textures and materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def normalize_mesh(vertices):
    min_bounds = np.min(vertices, axis=0)
    max_bounds = np.max(vertices, axis=0)

    bounds_diff = max_bounds - min_bounds
    scale = np.max(bounds_diff)
    return (vertices - min_bounds) / scale
