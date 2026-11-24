# get_cubic_bezier_points
#
# Copied verbatim from https://github.com/christian-vorhemus/procedural-3d-image-generation
#   file blenderBackgroundTask.py, line 38
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as np


def get_cubic_bezier_points(start, end, c1, c2, num_points=10, z_point=0):
    points = []
    for t in np.arange(0.0, 1.0, 1/num_points):
        x = math.pow((1-t),3)*start[0] + 3*t*math.pow((1-t),2)*c1[0] + 3*t*t*(1-t)*c2[0] + t*t*t*end[0]
        y = math.pow((1-t),3)*start[1] + 3*t*math.pow((1-t),2)*c1[1] + 3*t*t*(1-t)*c2[1] + t*t*t*end[1]
        points.append((x,y,z_point))
    return points
