# rotation_matrix
#
# Copied verbatim from https://github.com/lermert/noisi
#   file noisi/util/rotate_horizontal_components.py, line 20
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import cos
import numpy as np
from math import radians
from math import sin


def rotation_matrix(baz):
    baz_rad = radians(baz)
    rot_er = -sin(baz_rad)
    rot_nr = -cos(baz_rad)
    rot_et = -cos(baz_rad)
    rot_nt = sin(baz_rad)

    #return(rot_nr, rot_nt, rot_er, rot_et)
    return(np.asarray([[1, 0, 0], [0, rot_nr, rot_nt], [0, rot_er, rot_et]]))
