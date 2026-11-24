# dirichlet
#
# Copied verbatim from https://github.com/bsmithyman/pygeo
#   file util/dirichlet.py, line 79
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def kernelfunc (k, t):
  return np.cos(k * t)


def dirichlet (y, kys, weights=None):
  if (weights is None):
    weights = np.ones_like(kys) / len(kys)

  outseries = 0.5*kernelfunc(kys[0], y)*weights[0]
  for i, ky in enumerate(kys[1:]):
    outseries += kernelfunc(ky, y) * weights[i+1]

  return outseries
