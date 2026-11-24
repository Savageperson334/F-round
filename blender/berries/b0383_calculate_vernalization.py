# calculate_vernalization
#
# Copied verbatim from https://github.com/JohnnyHewson/Plant-Growth
#   file Project/Scripts/Tiller and Leaf Growth/Old Thermal Time Calculation.py, line 70
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plants and growth models
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import cos
from math import radians


def calculate_vernalization(T_min,T_max):
    T_min = max(T_min,0)
    T_max = max(T_max,0)
    V_eff = 0
    for r in range(1, 9):
        f_r = (1 / 2) * (1 + cos(radians((90 / 8) * ((2 * r) - 1))))
        T_H = max(T_min + f_r * (T_max - T_min), 0)  #Degree Celsius
        if -4 <= T_H < 3:
            V_eff += (T_H + 4) / 7
        elif 3 <= T_H <= 10:
            V_eff += 1
        elif 10 < T_H <= 17:
            V_eff += (17 - T_H) / 7
        else:
            V_eff += 0
    return (1/8)*V_eff
