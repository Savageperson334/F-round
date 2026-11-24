# calc_VDD
#
# Copied verbatim from https://github.com/JohnnyHewson/Plant-Growth
#   file Project/Scripts/Tiller and Leaf Growth/Simulation.py, line 154
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


def calc_VDD(T_max, T_min, VDD):
    T_min = max(T_min,0)
    T_max = max(T_max,0)

    if T_max > 30:
        VDD /= 2

    V_eff = 0
    for r in range(1,9):
        T_H = calc_T_H(T_max, T_min, r)
        if -4 <= T_H and T_H < 3:
            V_eff += (T_H + 4) / 7
        elif 3 <= T_H and T_H < 10:
            V_eff += 1
        elif 10 <= T_H and T_H < 17:
            V_eff += (17 - T_H) / 7

    VDD += (1/8) * V_eff

    return VDD
