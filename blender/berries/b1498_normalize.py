# normalize
#
# Copied verbatim from https://github.com/complight/Complex_Valued_Holographic_Radiance_Fields
#   file utils/colmap_dataloader.py, line 368
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def normalize(x):
    """Normalize a vector."""
    return x / np.linalg.norm(x)
