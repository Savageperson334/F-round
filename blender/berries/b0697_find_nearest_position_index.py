# find_nearest_position_index
#
# Copied verbatim from https://github.com/ScopeFoundry/ScopeFoundry
#   file sweeping/sweep_nd_base.py, line 1332
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def find_nearest_position_index(positions, target_positions) -> int:
    positions_array = np.array(positions)
    target_positions = np.array(target_positions)
    distances = np.linalg.norm(positions_array - target_positions, ord=2, axis=1)
    return int(np.argmin(distances))
