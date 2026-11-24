# removeNaN
#
# Copied verbatim from https://github.com/rsandler00/plotly-scientific-plots
#   file plotly_scientific_plots/misc_computational_tools.py, line 357
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def removeNaN(x):
    # This function removes NaNs
    return np.array(x)[~np.isnan(x)]
