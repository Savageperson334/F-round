# applyLookupTable
#
# Copied verbatim from https://github.com/JeremyPorquez/CRASHyperspectralAnalysis
#   file HSA/pyqtgraph/functions.py, line 977
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def applyLookupTable(data, lut):
    """
    Uses values in *data* as indexes to select values from *lut*.
    The returned data has shape data.shape + lut.shape[1:]

    Note: color gradient lookup tables can be generated using GradientWidget.
    """
    if data.dtype.kind not in ('i', 'u'):
        data = data.astype(int)

    return np.take(lut, data, axis=0, mode='clip')
