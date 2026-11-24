# calc_T_H
#
# Copied verbatim from https://github.com/JohnnyHewson/Plant-Growth
#   file Project/Scripts/Tiller and Leaf Growth/Simulation.py, line 89
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plants and growth models
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import cos
from math import pi


def calc_T_H(T_max, T_min, r):
    f_r = (1 / 2) * (1 + cos((90 / 8) * (2 * r - 1) * pi / 180))
    T_H = max(T_min + f_r * (T_max - T_min), 0)  # Degree Celsius

    return T_H
