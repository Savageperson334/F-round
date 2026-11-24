# lslope
#
# Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
#   file tools/research/ferrohydro/fluid.py, line 27
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ferrofluids and magnetic materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def lslope(x):
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    small = np.abs(x) < 1e-2
    xs = x[small]
    out[small] = 1 / 3 - xs * xs / 15 + 2 * xs ** 4 / 189
    xl = x[~small]
    out[~small] = 1 / xl ** 2 - 1 / np.sinh(xl) ** 2
    return out
