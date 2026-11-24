# signed_sqrt_transform
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file figs/signed_sqrt_transform/visualize_stats.py, line 19
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

GAMMA = 0.5


def signed_sqrt_transform(values):
    """Apply signed sqrt transform to elevation data"""
    return np.sign(values) * np.abs(values)**GAMMA
