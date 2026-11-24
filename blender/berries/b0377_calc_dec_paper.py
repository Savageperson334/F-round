# calc_dec_paper
#
# Copied verbatim from https://github.com/JohnnyHewson/Plant-Growth
#   file Project/Scripts/Data Visualization/DeclinationEquationComparison.py, line 15
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plants and growth models
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import asin
from math import pi
from math import sin


def calc_dec_paper(julian_day):
    theta_1 = 2*pi*(julian_day - 80) / 365
    theta_2 = 0.0335*(sin(2*pi*julian_day) - sin(2*pi*80)) / 365
    theta = theta_1 + theta_2

    declination = asin(0.3978*sin(theta))

    return declination
