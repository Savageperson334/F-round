# translation_matrix
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/util/transformations.py, line 220
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#   the same function also appears in: boschresearch/pcg_gazebo
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy


def translation_matrix(direction):
    """Return matrix to translate by direction vector.

    >>> v = numpy.random.random(3) - 0.5
    >>> numpy.allclose(v, translation_matrix(v)[:3, 3])
    True

    """
    M = numpy.identity(4)
    M[:3, 3] = direction[:3]
    return M
