# field_schedule
#
# Copied verbatim from https://github.com/efealtiparmakoglu/ferrofluid-cinema
#   file ferrofluid.py, line 411
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ferrofluids and magnetic materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def field_schedule(n_frames: int, b_start: float, b_end: float,
                   power: float = 1.0) -> np.ndarray:
    """Field ramp used by the animation: the magnet descends, the field grows."""
    t = np.linspace(0.0, 1.0, n_frames)
    return b_start + (b_end - b_start) * (t ** power)
