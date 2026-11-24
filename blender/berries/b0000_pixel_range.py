# pixel_range
#
# Copied verbatim from https://github.com/1202kbs/Understanding-NN
#   file utils.py, line 32
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def pixel_range(img):
	vmin, vmax = np.min(img), np.max(img)

	if vmin * vmax >= 0:
		return (vmin, vmax)
	else:

		if -vmin > vmax:
			vmax = -vmin
		else:
			vmin = -vmax

		return (vmin, vmax)
