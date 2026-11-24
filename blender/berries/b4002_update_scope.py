# update_scope
#
# Copied verbatim from https://github.com/xtai/Real-Time-Satellite-Tracking
#   file 3d-refactor-2.py, line 246
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def update_scope(current, min, max): # limit then keep
	if   current < min: return min
	elif current > max: return max
	else:               return current
