# sph2cart
#
# Copied verbatim from https://github.com/davofis/computational_seismology
#   notebook Aki_Rich_sol/double_coupled.ipynb (its code cells joined in order; line 14 of those)
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from numpy import cos
from numpy import sin


def sph2cart(r, th, phi):
    '''
    Transform spherical coordinates to cartesian
    '''
    x = r * sin(th) * cos(phi)
    y = r * sin(th) * sin(phi)
    z = r * cos(th)   
    return x, y, z
