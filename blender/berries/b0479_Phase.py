# Phase
#
# Copied verbatim from https://github.com/Ma-Weber/Tutorial-Deconvolution
#   notebook TutorialFinal.ipynb (its code cells joined in order; line 79 of those)
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Ocean hydrophones and acoustic ecology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def Phase(data):
    n = data.size
    return np.arctan2(data[int(n/2):],data[:int(n/2)])
