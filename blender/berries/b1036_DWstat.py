# DWstat
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 301
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def DWstat(data, model):
	residuals = data - model
	residual_difs = [] 
	for i in np.arange(1,len(residuals),1):
		residual_dif = residuals[i] - residuals[i-1]
		residual_difs.append(residual_dif)
	residual_difs = np.array(residual_difs)
	DWnum = np.nansum(residual_difs**2)
	DWdenom = np.nansum(residuals**2)
	DW = DWnum / DWdenom
	return DW
