# rotation_from_angle_and_axis
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/moment_tensor.py, line 49
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as num

r2d = 180. / math.pi

d2r = 1. / r2d


def rotation_from_angle_and_axis(angle, axis):
    '''
    Build rotation matrix based on axis and angle.

    :param angle: rotation angle [degrees]
    :param axis: orientation of rotation axis, either in spherical
        coordinates ``(theta, phi)`` [degrees], or as a unit vector
        ``(ux, uy, uz)``.
    '''

    if len(axis) == 2:
        theta, phi = axis
        ux = math.sin(d2r*theta)*math.cos(d2r*phi)
        uy = math.sin(d2r*theta)*math.sin(d2r*phi)
        uz = math.cos(d2r*theta)

    elif len(axis) == 3:
        axis = num.asarray(axis)
        uabs = math.sqrt(num.sum(axis**2))
        ux, uy, uz = axis / uabs
    else:
        assert False

    ct = math.cos(d2r*angle)
    st = math.sin(d2r*angle)
    return num.array([
        [ct + ux**2*(1.-ct), ux*uy*(1.-ct)-uz*st, ux*uz*(1.-ct)+uy*st],
        [uy*ux*(1.-ct)+uz*st, ct+uy**2*(1.-ct), uy*uz*(1.-ct)-ux*st],
        [uz*ux*(1.-ct)-uy*st, uz*uy*(1.-ct)+ux*st, ct+uz**2*(1.-ct)]
        ])
