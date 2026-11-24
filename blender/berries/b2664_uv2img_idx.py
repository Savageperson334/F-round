# uv2img_idx
#
# Copied verbatim from https://github.com/matsuren/crownconv360depth
#   file utils/projection_helper.py, line 118
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def uv2img_idx(uv, erp_img):
    h, w = erp_img.shape[:2]
    delta_w = 2 * np.pi / w
    delta_h = np.pi / h
    x = uv[..., 0] / delta_w + w / 2 - 0.5
    y = uv[..., 1] / delta_h + h / 2 - 0.5
    x = np.clip(x, 0, w - 1)
    y = np.clip(y, 0, h - 1)
    return np.stack([y, x], axis=0)
