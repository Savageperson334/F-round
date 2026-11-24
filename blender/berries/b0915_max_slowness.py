# max_slowness
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook dev/Ray-tracing.ipynb (its code cells joined in order; line 20 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def max_slowness(v):
    p = 1/np.max(v)
    return p
