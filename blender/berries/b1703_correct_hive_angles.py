# correct_hive_angles
#
# Copied verbatim from https://github.com/ericmjl/nxviz
#   file nxviz/geometry.py, line 70
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def correct_hive_angles(start, end):
    """Perform correction of hive plot angles for edge drawing."""
    if start > np.pi and end == 0.0:
        end = 2 * np.pi
    if start < np.pi and end == 0.0:
        start, end = end, start
    if end < np.pi and start == 2 * np.pi:
        start = 0
    if end > np.pi and start == 0:
        start = 2 * np.pi
    return start, end
