# frequencies
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/particles.py, line 371
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

PAD = 4


def frequencies(s: int) -> np.ndarray:
    """The frequencies a stretch of S games is read at, a game⁻¹: from 1/S (a period of S games) to 1/2."""
    return np.arange(PAD, PAD * s // 2 + 1) / (PAD * s)
