# correlated_sum
#
# Copied verbatim from https://github.com/mdaeron/D47crunch
#   file src/D47crunch/__init__.py, line 88
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def correlated_sum(X, C, w = None):
	'''
	Compute covariance-aware linear combinations

	**Parameters**

	+ `X`: list or 1-D array of values to sum
	+ `C`: covariance matrix for the elements of `X`
	+ `w`: list or 1-D array of weights to apply to the elements of `X`
	       (all equal to 1 by default)

	Return the sum (and its SE) of the elements of `X`, with optional weights equal
	to the elements of `w`, accounting for covariances between the elements of `X`.
	'''
	if w is None:
		w = [1 for x in X]
	return np.dot(w,X), (np.dot(w,np.dot(C,w)))**.5
