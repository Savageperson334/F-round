# transit_SNR
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 194
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def transit_SNR(depth, error_per_obs, transit_duration_minutes):
	### SIMPLE TRANSIT SNR CALCULATOR -- DOESN'T ACCOUNT FOR TRANSIT MORPHOLOGY.
	return (depth/error_per_obs) * np.sqrt((transit_duration_minutes / 30))
