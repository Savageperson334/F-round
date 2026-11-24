# mass_from_density
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 120
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def mass_from_density(density, radius):
	### density and radius should have matching units!
	object_volume = (4/3) * np.pi * radius**3
	object_mass = density * object_volume
	return object_mass
