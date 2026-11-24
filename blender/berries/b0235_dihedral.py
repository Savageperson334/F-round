# dihedral
#
# Copied verbatim from https://github.com/Flowm/satvis
#   file scripts/starmap/cubemap.py, line 410
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def dihedral(img: np.ndarray, k: int) -> np.ndarray:
    """The eight square symmetries, for the orientation check."""
    out = np.rot90(img, k % 4)
    return np.fliplr(out) if k >= 4 else out
