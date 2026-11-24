# mode
#
# Copied verbatim from https://github.com/JeremyPorquez/CRASHyperspectralAnalysis
#   file HSA/pyqtgraph/flowchart/library/functions.py, line 129
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def mode(data, bins=None):
    """Returns location max value from histogram."""
    if bins is None:
        bins = int(len(data)/10.)
        if bins < 2:
            bins = 2
    y, x = np.histogram(data, bins=bins)
    ind = np.argmax(y)
    mode = 0.5 * (x[ind] + x[ind+1])
    return mode
