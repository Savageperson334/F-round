# flux_from_mags
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_tools.py, line 314
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def flux_from_mags(target_mag, ref_mag, ref_flux):
	### computes the flux based on a known target magnitude, reference magnitude, and reference flux.
	target_flux = ref_flux * 10**( (ref_mag - target_mag) / 2.5)
	return target_flux
