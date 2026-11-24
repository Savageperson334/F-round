# contorl_opp
#
# Copied verbatim from https://github.com/xtai/Real-Time-Satellite-Tracking
#   file 3d-refactor-2.py, line 302
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def contorl_opp(key, var, step):
	if   key[0]: var += step
	elif key[1]: var -= step
	return var
