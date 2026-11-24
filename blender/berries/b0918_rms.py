# rms
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks/Windowed_attribute_statistics.ipynb (its code cells joined in order; line 25 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rms(data):
    """
    Root mean square.

    Example
    >>> rms([3, 4, 5])
    4.08248290463863
    """
    data = np.asanyarray(data)
    return np.sqrt(np.sum(data**2) / data.size)
