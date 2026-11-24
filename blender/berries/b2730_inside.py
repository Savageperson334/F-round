# inside
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/src/utils/psf_gui_qt.py, line 53
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def inside(shape, center, window):
    """A bead's fitting window must fit inside the volume with room to spare.
    Strict inequalities: a window that exactly touches the edge leaves zero
    margin, so there's no guarantee the profile has decayed back to baseline
    within it (e.g. a bead sitting right at the top/bottom of the acquired
    Z-stack)."""
    return np.all([
        (center[i] - window[i] // 2 > 0) &
        (center[i] + window[i] // 2 < shape[i])
        for i in range(3)
    ])
