# calculate_rmse
#
# Copied verbatim from https://github.com/JohnnyHewson/Plant-Growth
#   file Project/Archive/Scripts/Data Interpolator/RSME Graph.py, line 6
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plants and growth models
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def calculate_rmse(series1, series2):
    """Calculate RMSE for two series."""
    return np.sqrt(np.mean((series1 - series2) ** 2))
