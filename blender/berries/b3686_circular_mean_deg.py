# circular_mean_deg
#
# Copied verbatim from https://github.com/strangeloopcanon/paleontology_analytics
#   file thesis/_lib/__init__.py, line 136
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def circular_mean_deg(longitudes_deg: np.ndarray) -> float:
    """Directional (circular) mean of angles in degrees."""
    rad = np.deg2rad(longitudes_deg)
    s = float(np.nanmean(np.sin(rad)))
    c = float(np.nanmean(np.cos(rad)))
    return float(np.rad2deg(np.arctan2(s, c)))
