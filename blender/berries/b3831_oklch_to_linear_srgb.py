# oklch_to_linear_srgb
#
# Copied verbatim from https://github.com/touchbr/Graphite
#   file scripts/soften_colormap.py, line 214
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def oklch_to_linear_srgb(lightness: float, chroma: float, hue: float) -> tuple[float, float, float]:
    hue_radians = math.radians(hue)
    lab_a = chroma * math.cos(hue_radians)
    lab_b = chroma * math.sin(hue_radians)

    long_root = lightness + 0.3963377774 * lab_a + 0.2158037573 * lab_b
    medium_root = lightness - 0.1055613458 * lab_a - 0.0638541728 * lab_b
    short_root = lightness - 0.0894841775 * lab_a - 1.2914855480 * lab_b

    long = long_root**3
    medium = medium_root**3
    short = short_root**3

    red = 4.0767416621 * long - 3.3077115913 * medium + 0.2309699292 * short
    green = -1.2684380046 * long + 2.6097574011 * medium - 0.3413193965 * short
    blue = -0.0041960863 * long - 0.7034186147 * medium + 1.7076147010 * short
    return red, green, blue
