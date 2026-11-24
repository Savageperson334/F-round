# deviation
#
# Copied verbatim from https://github.com/ygd551/terra-incognita
#   file ros1_ws/scripts/isaac_adapter.py, line 72
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def deviation(path, pos, dims=2):
    """Distance from pos to the path (polyline), in xy or, dims=3, in 3D: how far the robot is off the planned path."""
    a, b = path[:-1, :dims], path[1:, :dims]
    ab = b - a
    t = np.clip(((pos[:dims] - a) * ab).sum(1) / np.maximum((ab * ab).sum(1), 1e-12), 0.0, 1.0)
    return float(np.linalg.norm(a + t[:, None] * ab - pos[:dims], axis=1).min())
