# AIP
#
# Copied verbatim from https://github.com/davofis/computational_seismology
#   notebook Aki_Rich_sol/double_coupled.ipynb (its code cells joined in order; line 77 of those)
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from numpy import asarray
from numpy import cos
from numpy import sin


def AIP(th, phi):    
    AIP = [[4*sin(2*th)*cos(phi), -2*cos(2*th)*cos(phi), 2*cos(th)*sin(phi)]]
    return asarray(AIP)
