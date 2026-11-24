# sigma2fwhm
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/src/utils/optimization.py, line 63
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def sigma2fwhm(sigma):
    """Convert gaussian std (sigma) to full-width half-maximum (FWHM)"""
    return 2.0 * sigma * np.sqrt(2 * np.log(2))
