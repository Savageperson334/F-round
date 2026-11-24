# density_conversion
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 199
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def density_conversion(mass, radius, munit='kg', runit='meters'):
	rho_obj = mass / ((4/3) * np.pi * radius**3)
	return rho_obj
