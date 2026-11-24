# langevin
#
# Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
#   file tools/research/ferrohydro/fluid.py, line 16
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ferrofluids and magnetic materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def langevin(x):
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    small = np.abs(x) < 1e-2
    xs = x[small]
    out[small] = xs * (1 / 3 - xs * xs / 45 + 2 * xs ** 4 / 945)
    xl = x[~small]
    out[~small] = 1 / np.tanh(xl) - 1 / xl
    return out
