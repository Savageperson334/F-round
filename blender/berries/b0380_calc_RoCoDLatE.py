# calc_RoCoDLatE
#
# Copied verbatim from https://github.com/JohnnyHewson/Plant-Growth
#   file Project/Scripts/Tiller and Leaf Growth/Old Simulation.py, line 110
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plants and growth models
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import cos
from math import pi
from math import radians
from math import sin
from math import sqrt


def calc_RoCoDLatE(latitude, julian_day):
    tilt_of_earth = 23.44 * (pi / 180) #Converts to radians
    radians_per_day = 2*pi * (1 / 365.25)

    latitude_rad = radians(latitude)
    declination = -tilt_of_earth * cos(radians_per_day * (julian_day + 10))
    declination_rate = (tilt_of_earth * radians_per_day * sin(radians_per_day * (julian_day + 10)))

    numerator = cos(declination) * sin(latitude_rad)
    denominator = sqrt((1 - (sin(latitude_rad) * sin(declination)))**2)

    if denominator == 0:
        return 0.0
    else:
        return (24 / pi) * (numerator / denominator) * declination_rate
