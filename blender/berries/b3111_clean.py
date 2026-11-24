# clean
#
# Copied verbatim from https://github.com/praneshnikhar/OceanScope3D
#   file backend/app/api/routes.py, line 25
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ocean currents and fluid dynamics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def clean(arr: np.ndarray):
    arr = np.asarray(arr, dtype="float64")
    return np.where(np.isfinite(arr), arr, None).tolist()
