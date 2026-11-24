# impact_from_inc
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 136
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def impact_from_inc(inclination, rstar, sma, unit='degrees'):
	### units must be consistent!
	if unit == 'degrees':
		inclination = inclination * (np.pi / 180)
	impact = (sma * np.cos(inclination)) / rstar
	return impact
