# inverse_signed_sqrt_transform
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file figs/signed_sqrt_transform/visualize_stats.py, line 23
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

GAMMA = 0.5


def inverse_signed_sqrt_transform(values):
    """Invert the signed sqrt transform to get back original elevation"""
    return np.sign(values) * np.abs(values)**(1/GAMMA)
