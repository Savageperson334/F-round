# coord2pix
#
# Copied verbatim from https://github.com/alexteachey/MoonPy
#   file mp_animate.py, line 47
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def coord2pix(coord, ref_pixel, ref_coord, pixel_size_deg):
	#print('calling coord2pix.')
	#### takes in a coordinate and gives you the pixel value
	delta_coord = coord - ref_coord 
	delta_pixel = delta_coord / pixel_size_deg 
	output_pixel = delta_pixel + ref_pixel 
	return output_pixel
