# norm_range
#
# Copied verbatim from https://github.com/conan7882/CNN-Visualization
#   file lib/utils/normalize.py, line 30
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def norm_range(filter_in):
    f_min = np.amin(filter_in)
    f_max = np.amax(filter_in)

    return (filter_in - f_min) * 1.0 / (f_max + 1e-5) * 255.0
