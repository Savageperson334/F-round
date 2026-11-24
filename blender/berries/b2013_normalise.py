# normalise
#
# Copied verbatim from https://github.com/gorliks/OpenECCI-GUI
#   file src/utils.py, line 43
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def normalise(image):
    norm = np.linalg.norm(image)
    image_norm = image / norm  # normalized matrix
    return image_norm
