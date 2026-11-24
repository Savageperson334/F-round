# quaternion_conjugate
#
# Copied verbatim from https://github.com/boschresearch/pcg_gazebo
#   file pcg_gazebo/transformations.py, line 1245
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy


def quaternion_conjugate(quaternion):
    """Return conjugate of quaternion.

    >>> q0 = random_quaternion()
    >>> q1 = quaternion_conjugate(q0)
    >>> q1[3] == q0[3] and all(q1[:3] == -q0[:3])
    True

    """
    return numpy.array((-quaternion[0], -quaternion[1],
                        -quaternion[2], quaternion[3]), dtype=numpy.float64)
