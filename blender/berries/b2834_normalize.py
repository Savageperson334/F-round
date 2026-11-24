# normalize
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file util.py, line 72
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy


def normalize(v: numpy.ndarray) -> numpy.ndarray:
    '''Return the vector, but scaled to length 1.'''
    norm = numpy.linalg.norm(v)
    result = v / norm
    assert isinstance(result, numpy.ndarray)
    return result
