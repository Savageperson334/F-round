# iterate
#
# Copied verbatim from https://github.com/nofelmahmood/ArtificialLife
#   file Predator-Prey/Predator-Prey.py, line 23
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def predator(x, y, a, b, e):
	return x + a*x + b*y + e*x*x


def prey(x, y, c, d, f):
	return y + c*x + d*y + f*y*y


def iterate(a, iterations):

	x = np.zeros(iterations + 1, dtype=float)
	y = np.zeros(iterations + 1, dtype=float)

	x[0] = 1000.0
	y[0] = 500.0

	# Set values for all constants to produce a stable osscilation.
	b = -3
	e = 0.0000001
	c = 0.3
	d = -2
	f = 0.00001

	# Iterate to calculate next states.
	for i in range(0, iterations):
		x[i + 1] = predator(x[i], y[i], a, b, e)
		y[i + 1] = prey(x[i], y[i], c, d, f)


	return (x, y)
