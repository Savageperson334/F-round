# gauss
#
# Copied verbatim from https://github.com/topherchris420/nocturne
#   file vdl7/spectral.py, line 114
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def gauss(lam: float, mu: float, fwhm: float) -> float:
    sigma = fwhm / 2.354820045
    return math.exp(-0.5 * ((lam - mu) / sigma) ** 2)
