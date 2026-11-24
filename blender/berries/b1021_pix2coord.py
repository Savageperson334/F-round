# pix2coord
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_animate.py, line 39
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def pix2coord(pixel, ref_pixel, ref_coord, pixel_size_deg):
	#print('calling pix2coord.')
	#### takes a given pixel value and gives you the coordinate value.
	delta_pixel = pixel - ref_pixel  ### degrees
	delta_coord = delta_pixel * pixel_size_deg 
	output_coord = delta_coord + ref_coord
	return output_coord
