# subsample
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks_dev/Time-depth_conversion_hacking.ipynb (its code cells joined in order; line 65 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def subsample(arr, d0, dnew):
    r = int(d0 / dnew)
    return np.repeat(arr, r)
