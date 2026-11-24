# is_same_quaternion
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/util/transformations.py, line 1884
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy


def is_same_quaternion(q0, q1):
    """Return True if two quaternions are equal."""
    q0 = numpy.array(q0)
    q1 = numpy.array(q1)
    return numpy.allclose(q0, q1) or numpy.allclose(q0, -q1)
