# arcball_map_to_sphere
#
# Copied verbatim from https://github.com/boschresearch/pcg_gazebo
#   file pcg_gazebo/transformations.py, line 1472
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy


def arcball_map_to_sphere(point, center, radius):
    """Return unit sphere coordinates from window coordinates."""
    v = numpy.array(((point[0] - center[0]) / radius,
                     (center[1] - point[1]) / radius,
                     0.0), dtype=numpy.float64)
    n = v[0] * v[0] + v[1] * v[1]
    if n > 1.0:
        v /= math.sqrt(n)  # position outside of sphere
    else:
        v[2] = math.sqrt(1.0 - n)
    return v
