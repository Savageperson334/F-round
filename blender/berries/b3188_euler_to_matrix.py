# euler_to_matrix
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/moment_tensor.py, line 264
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as num


def euler_to_matrix(alpha, beta, gamma):
    '''
    Given euler angle triplet, create rotation matrix

    Given coordinate system `(x,y,z)` and rotated system `(xs,ys,zs)`
    the line of nodes is the intersection between the `x,y` and the `xs,ys`
    planes.

    :param alpha: is the angle between the `z`-axis and the `zs`-axis [rad]
    :param beta:  is the angle between the `x`-axis and the line of nodes [rad]
    :param gamma: is the angle between the line of nodes and the `xs`-axis
        [rad]

    Usage for moment tensors::

        m_unrot = numpy.array([[0,0,-1],[0,0,0],[-1,0,0]])
        euler_to_matrix(dip,strike,-rake, rotmat)
        m = num.dot(rotmat.T, num.dot(m_unrot, rotmat))

    '''

    ca = math.cos(alpha)
    cb = math.cos(beta)
    cg = math.cos(gamma)
    sa = math.sin(alpha)
    sb = math.sin(beta)
    sg = math.sin(gamma)

    mat = num.array([[cb*cg-ca*sb*sg,  sb*cg+ca*cb*sg,  sa*sg],
                     [-cb*sg-ca*sb*cg, -sb*sg+ca*cb*cg, sa*cg],
                     [sa*sb,           -sa*cb,          ca]], dtype=float)
    return mat
