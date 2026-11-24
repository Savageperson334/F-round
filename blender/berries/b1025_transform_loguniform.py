# transform_loguniform
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_fit.py, line 45
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def transform_loguniform(x,lower,upper):
	l_lower=np.log10(lower)
	l_upper=np.log10(upper)
	valrange = l_upper - l_lower 
	#return np.exp(l_lower + x*(l_upper-l_lower))
	return 10**(l_lower + (valrange * x))
