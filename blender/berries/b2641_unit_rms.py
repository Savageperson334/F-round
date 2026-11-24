# unit_rms
#
# Copied verbatim from https://github.com/marksweiss/tastywaves
#   file tools/gen_wavetables.py, line 55
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def unit_rms(c):
    """Scale a spectrum to unit RMS (equal loudness across frames before the per-table gain)."""
    e = np.sqrt(np.sum(np.abs(c) ** 2) / 2)
    return c / e if e > 0 else c
