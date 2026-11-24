# process_image
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file terrain_diffusion/inference/dev_utils/visualize_noise.py, line 16
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def process_image(img):
    # Crop to middle 2/3rds (remove first and last 30 degrees of latitude)
    h = img.shape[0]
    crop_start = h // 6
    crop_end = h - h // 6
    img = img[crop_start:crop_end, :]
    img[img < -30000] = np.nan
    return img
