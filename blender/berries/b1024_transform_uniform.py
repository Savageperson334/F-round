# transform_uniform
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_fit.py, line 41
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def transform_uniform(x,lower,upper):
	valrange = upper - lower 
	return lower + (valrange)*x
