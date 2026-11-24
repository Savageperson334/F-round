# transpose_table
#
# Copied verbatim from https://github.com/mdaeron/D47crunch
#   file src/D47crunch/__init__.py, line 232
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def transpose_table(x):
	'''
	Transpose a list if lists

	**Parameters**

	+ `x`: a list of lists

	**Example**

	```py
	x = [[1, 2], [3, 4]]
	print(transpose_table(x)) # yields: [[1, 3], [2, 4]]
	```
	'''
	return [[e for e in c] for c in zip(*x)]
