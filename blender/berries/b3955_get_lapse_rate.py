# get_lapse_rate
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file terrain_diffusion/inference/dev_utils/visualize_noise.py, line 31
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_lapse_rate(precip):
    lapse_rate = -6.5 + 0.0015 * precip
    lapse_rate = np.clip(lapse_rate, -9.8, -4.0)
    return lapse_rate / 1000
