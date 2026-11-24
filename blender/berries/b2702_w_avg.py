# w_avg
#
# Copied verbatim from https://github.com/mdaeron/D47crunch
#   file src/D47crunch/__init__.py, line 250
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def w_avg(X, sX) :
	'''
	Compute variance-weighted average

	Returns the value and SE of the weighted average of the elements of `X`,
	with relative weights equal to their inverse variances (`1/sX**2`).

	**Parameters**

	+ `X`: array-like of elements to average
	+ `sX`: array-like of the corresponding SE values

	**Tip**

	If `X` and `sX` are initially arranged as a list of `(x, sx)` doublets,
	they may be rearranged using `zip()`:

	```python
	foo = [(0, 1), (1, 0.5), (2, 0.5)]
	print(w_avg(*zip(*foo))) # yields: (1.3333333333333333, 0.3333333333333333)
	```
	'''
	X = [ x for x in X ]
	sX = [ sx for sx in sX ]
	W = [ sx**-2 for sx in sX ]
	W = [ w/sum(W) for w in W ]
	Xavg = sum([ w*x for w,x in zip(W,X) ])
	sXavg = sum([ w**2*sx**2 for w,sx in zip(W,sX) ])**.5
	return Xavg, sXavg
