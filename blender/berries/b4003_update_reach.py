# update_reach
#
# Copied verbatim from https://github.com/xtai/Real-Time-Satellite-Tracking
#   file 3d-refactor-2.py, line 251
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def update_reach(current, min, max): # limit then swap
	if   current < min: return max
	elif current > max: return min
	else:               return current
