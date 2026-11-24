# effective_radius
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 91
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def effective_radius(density, mass):
	### CALCULATE AN EFFECTIVE RADIUS OF THE MOON FROM A PROVIDED MASS AND DENSITY -- DIFFERENT FROM EQUATORIAL!
	return ((3/4) * (mass/(np.pi * density)))**(1/3)
