# amplitude
#
# Copied verbatim from https://github.com/catrujilla/pyDHM
#   file pyDHM/phaseCompensation.py, line 654
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def amplitude(inp, log):
    out = np.abs(inp)

    if log == True:
        out = 20 * np.log(out)

    return out
