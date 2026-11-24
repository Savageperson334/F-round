# overlay_label_on_image01
#
# Copied verbatim from https://github.com/umfieldrobotics/ShipwreckFinderQGISPlugin
#   file utils/visualization_utils.py, line 102
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Shipwrecks and maritime ghosts
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def overlay_label_on_image01(image01_hwc, label01_hw, alpha=0.4):
    color_label = np.zeros((*label01_hw.shape, 3), dtype=np.float32)
    color_label[label01_hw == 1] = [1.0, 0.0, 0.0]  # red
    return (1 - alpha) * image01_hwc + alpha * color_label
