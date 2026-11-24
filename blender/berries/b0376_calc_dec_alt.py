# calc_dec_alt
#
# Copied verbatim from https://github.com/JohnnyHewson/Plant-Growth
#   file Project/Scripts/Data Visualization/DeclinationEquationComparison.py, line 8
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plants and growth models
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import cos
from math import pi


def calc_dec_alt(julian_day):
    tilt_of_earth = 23.44 * (pi / 180) #Converts to radians
    radians_per_day = 2*pi * (1 / 365.25)
    declination = -tilt_of_earth * cos(radians_per_day * (julian_day + 10))

    return declination
