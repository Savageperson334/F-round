# iterate_extended_terms
#
# Copied verbatim from https://github.com/nofelmahmood/ArtificialLife
#   file Predator-Prey/Predator-Prey.py, line 46
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


def iterate_extended_terms(a, iterations):

	x = np.zeros(iterations + 1, dtype=float)
	y = np.zeros(iterations + 1, dtype=float)

	x[0] = 1000.0
	y[0] = 500.0

	# Set values for all constants to produce a stable osscilation.
	b = -3
	e = 0.0000001
	g = 0
	c = 0.3
	d = -2
	f = 0.00001
	h = 0

	# extended terms
	g = 0.00001
	h = 0.00001

	for i in range(0, iterations):
		x[i + 1] = predator(x[i], y[i], a, b, e) + g * x[i] * y[i]
		y[i + 1] = prey(x[i], y[i], c, d, f) + h * x[i] * y[i]

	return (x, y)
