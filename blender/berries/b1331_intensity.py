# intensity
#
# Copied verbatim from https://github.com/catrujilla/pyDHM
#   file pyDHM/utilities.py, line 277
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def intensity(inp, log):
    out = np.abs(inp)
    if log == False or log == None:
        out = out * out
    else:
        out = 20 * np.log(out)
        out[out == np.inf] = 0
        out[out == -np.inf] = 0

    return out
