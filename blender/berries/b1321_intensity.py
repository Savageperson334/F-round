# intensity
#
# Copied verbatim from https://github.com/catrujilla/pyDHM
#   file pyDHM/phaseCompensation.py, line 640
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def intensity(inp, log):
    # Inputs:
    # inp - The input complex field
    # log - boolean variable to determine if a log representation is applied

    out = np.abs(inp)
    out = out * out

    if log == True:
        out = 20 * np.log(out)

    return out
