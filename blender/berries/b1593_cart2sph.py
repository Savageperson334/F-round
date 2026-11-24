# cart2sph
#
# Copied verbatim from https://github.com/davofis/computational_seismology
#   notebook Aki_Rich_sol/double_coupled.ipynb (its code cells joined in order; line 23 of those)
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from numpy import arccos
from numpy import arctan
from numpy import sqrt


def cart2sph(x, y, z):
    '''
    Transform cartesian coordinates to spherical
    '''
    r = sqrt(x**2 + y**2 + z**2)
    th = arccos(z/r)
    phi = arctan(y/x)
    return r, th, phi
