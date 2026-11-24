# linear_srgb_to_oklab
#
# Copied verbatim from https://github.com/touchbr/Graphite
#   file scripts/soften_colormap.py, line 199
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def linear_srgb_to_oklab(red: float, green: float, blue: float) -> tuple[float, float, float]:
    long = 0.4122214708 * red + 0.5363325363 * green + 0.0514459929 * blue
    medium = 0.2119034982 * red + 0.6806995451 * green + 0.1073969566 * blue
    short = 0.0883024619 * red + 0.2817188376 * green + 0.6299787005 * blue

    long_root = math.copysign(abs(long) ** (1 / 3), long)
    medium_root = math.copysign(abs(medium) ** (1 / 3), medium)
    short_root = math.copysign(abs(short) ** (1 / 3), short)

    lightness = 0.2104542553 * long_root + 0.7936177850 * medium_root - 0.0040720468 * short_root
    lab_a = 1.9779984951 * long_root - 2.4285922050 * medium_root + 0.4505937099 * short_root
    lab_b = 0.0259040371 * long_root + 0.7827717662 * medium_root - 0.8086757660 * short_root
    return lightness, lab_a, lab_b
