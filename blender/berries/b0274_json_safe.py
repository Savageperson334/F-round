# json_safe
#
# Copied verbatim from https://github.com/GalaxyUrsa/Pisces-Explorer
#   file backend/features/region/interpolation.py, line 16
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ocean currents and fluid dynamics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def json_safe(value):
    """Replace non-finite values in a Region response with JSON null."""
    if isinstance(value, dict):
        return {key: json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, np.ndarray):
        return json_safe(value.tolist())
    if isinstance(value, (float, np.floating)) and not np.isfinite(value):
        return None
    return value
