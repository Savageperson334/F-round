# quaternion_imag
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/util/transformations.py, line 1419
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy


def quaternion_imag(quaternion):
    """Return imaginary part of quaternion.

    >>> quaternion_imag([3, 0, 1, 2])
    array([ 0.,  1.,  2.])

    """
    return numpy.array(quaternion[1:4], dtype=numpy.float64, copy=True)
