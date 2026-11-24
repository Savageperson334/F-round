# wavy
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks/Wedges.ipynb (its code cells joined in order; line 144 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def wavy(start, stop, num):
    """
    Custom wedge shape.
    """
    x = np.linspace(0, 10*np.pi, num)
    y = np.sin(x) + x

    # Normalize to 0-1.
    y_ = (y - np.min(y)) / (np.max(y)-np.min(y))

    # Scale to required output.
    return min(start, stop) + abs(stop-start) * y_
