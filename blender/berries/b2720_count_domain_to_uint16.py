# count_domain_to_uint16
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/src/plugins/utils.py, line 16
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def count_domain_to_uint16(image: np.ndarray) -> np.ndarray:
    """Convert count-domain image data to uint16 with clipping."""
    image = np.asarray(image)
    image = np.nan_to_num(image, nan=0.0, posinf=65535.0, neginf=0.0)
    image = np.clip(np.rint(image), 0, 65535)
    return image.astype(np.uint16, copy=False)
