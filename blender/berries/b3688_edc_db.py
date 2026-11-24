# edc_db
#
# Copied verbatim from https://github.com/styvesgoupil/frasil
#   file tools/bench/analyze.py, line 32
#   licence (as GitHub reports it): MPL-2.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def edc_db(h):
    e = np.cumsum((h ** 2)[::-1])[::-1]
    return 10 * np.log10(e / e[0] + 1e-30)
