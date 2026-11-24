# inc_from_impact
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 126
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def inc_from_impact(impact, rstar, sma, unit='radians'):
	### units must be consistent!
	inclination = np.arccos((impact * rstar)/sma)
	if unit == 'degrees':
		inclination = (inclination * (180 / np.pi))
	else:
		inclination = inclination
	return inclination
