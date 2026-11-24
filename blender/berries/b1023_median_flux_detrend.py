# median_flux_detrend
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_detrend.py, line 91
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def median_flux_detrend(times, fluxes, errors):
	### simply divides out the median value of the fluxes -- should do this on a quarter-by-quarter basis, obviously

	flux_detrend = fluxes / np.nanmedian(fluxes)
	errors_detrend = errors / fluxes 

	#### for the sake of uniformity with other detrending functions
	best_model = np.linspace(np.nanmedian(fluxes), np.nanmedian(fluxes), len(fluxes))

	return best_model, flux_detrend, errors_detrend
