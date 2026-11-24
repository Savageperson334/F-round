# quadsum
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 151
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def quadsum(values):
	### SUM VALUES IN QUADRATURE
	return np.sqrt(np.sum(values**2))
