# pf
#
# Copied verbatim from https://github.com/mdaeron/D47crunch
#   file src/D47crunch/__init__.py, line 133
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def pf(txt):
	'''
	Modify string `txt` to follow `lmfit.Parameter()` naming rules.
	'''
	return txt.replace('-','_').replace('.','_').replace(' ','_')
