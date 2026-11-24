# dircos
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file fatiando/utils.py, line 322
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy


def dircos(inc, dec):
    """
    Returns the 3 coordinates of a unit vector given its inclination and
    declination.

    .. note:: Coordinate system is assumed to be x->North, y->East, z->Down.
        Inclination is positive down and declination is measured with respect
        to x (North).

    Parameter:

    * inc : float
        The inclination of the vector (in degrees)
    * dec : float
        The declination of the vector (in degrees)

    Returns:

    * vect : list = [x, y, z]
        The unit vector

    """
    d2r = numpy.pi / 180.
    vect = [numpy.cos(d2r * inc) * numpy.cos(d2r * dec),
            numpy.cos(d2r * inc) * numpy.sin(d2r * dec),
            numpy.sin(d2r * inc)]
    return vect
