# u1u2_to_q1q2
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 162
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def u1u2_to_q1q2(u1, u2): 
	### this function converts the standard, quadratic limb darkening coefficents to 
	### David Kipping's q1 and q2, which are the standard inputs for LUNA. 
	### see arXiv 1308.0009 equations 17 and 18 for this reparameterization
	q1 = (u1 + u2)**2
	q2 = (0.5 * u1) / (u1 + u2)
	return q1, q2
