# generate_color
#
# Copied verbatim from https://github.com/paulgb/penkit
#   file optimizer/penkit_optimize/visualize.py, line 6
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import colorsys


def generate_color(hue, saturation=1.0, value=1.0):
    rgb = colorsys.hsv_to_rgb(hue, saturation, value)
    return "rgb({},{},{})".format(*[int(x * 255) for x in rgb])
