# q1q2_to_u1u2
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 170
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def q1q2_to_u1u2(q1, q2):
	u1 = 2*q2*np.sqrt(q1)
	u2 = -2*(q2 - 0.5) * np.sqrt(q1)
	return u1, u2
