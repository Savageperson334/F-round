# normalized_to_uint16
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/src/plugins/utils.py, line 24
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def normalized_to_uint16(image: np.ndarray) -> np.ndarray:
    """Convert normalized float data in the range [0, 1] to uint16."""
    image = np.asarray(image)
    image = np.nan_to_num(image, nan=0.0, posinf=1.0, neginf=0.0)
    image = np.clip(image, 0.0, 1.0)
    image = np.rint(image * 65535.0)
    return image.astype(np.uint16, copy=False)
