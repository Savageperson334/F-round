# arcball_map_to_sphere
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/util/transformations.py, line 1624
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy


def arcball_map_to_sphere(point, center, radius):
    """Return unit sphere coordinates from window coordinates."""
    v0 = (point[0] - center[0]) / radius
    v1 = (center[1] - point[1]) / radius
    n = v0*v0 + v1*v1
    if n > 1.0:
        # position outside of sphere
        n = math.sqrt(n)
        return numpy.array([v0/n, v1/n, 0.0])
    else:
        return numpy.array([v0, v1, math.sqrt(1.0 - n)])
