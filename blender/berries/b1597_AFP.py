# AFP
#
# Copied verbatim from https://github.com/davofis/computational_seismology
#   notebook Aki_Rich_sol/double_coupled.ipynb (its code cells joined in order; line 85 of those)
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from numpy import asarray
from numpy import cos
from numpy import sin


def AFP(th, phi):    
    AFP = [sin(2*th)*cos(phi), 0, 0 ]
    return asarray(AFP)
