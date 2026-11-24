# make_csv
#
# Copied verbatim from https://github.com/mdaeron/D47crunch
#   file src/D47crunch/__init__.py, line 107
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def make_csv(x, hsep = ',', vsep = '\n'):
	'''
	Formats a list of lists of strings as a CSV

	**Parameters**

	+ `x`: the list of lists of strings to format
	+ `hsep`: the field separator (`,` by default)
	+ `vsep`: the line-ending convention to use (`\\n` by default)

	**Example**

	```py
	print(make_csv([['a', 'b', 'c'], ['d', 'e', 'f']]))
	```

	outputs:

	```py
	a,b,c
	d,e,f
	```
	'''
	return vsep.join([hsep.join(l) for l in x])
