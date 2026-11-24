# get_density_from_barometric_formula
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/atmosphere/models.py, line 346
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_density_from_barometric_formula(hh):
    """ returns the atmospheric density [g/m^3] for the height h abolve see level
    according to https://en.wikipedia.org/wiki/Barometric_formula"""
    if isinstance(hh, float):
        hh = np.array([hh])
    R = 8.31432  # universal gas constant for air: 8.31432 N m/(mol K)
    g0 = 9.80665  # gravitational acceleration (9.80665 m/s2)
    M = 0.0289644  # molar mass of Earth's air (0.0289644 kg/mol)
    rhob = [1.2250, 0.36391, 0.08803, 0.01322, 0.00143, 0.00086, 0.000064]
    Tb = [288.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65]
    Lb = [-0.0065, 0, 0.001, 0.0028, 0, -0.0028, -0.002]
    hb = [0, 11000, 20000, 32000, 47000, 51000, 71000]

    def rho1(h, i):  # for Lb != 0
        return rhob[i] * (Tb[i] / (Tb[i] + Lb[i] * (h - hb[i]))) ** (1 + (g0 * M) / (R * Lb[i]))

    def rho2(h, i):  # for Lb == 0
        return rhob[i] * np.exp(-g0 * M * (h - hb[i]) / (R * Tb[i]))

    densities = np.zeros_like(hh)
    for i, h in enumerate(hh):
        if (h < 0):
            densities[i] = np.nan
        elif(h > 86000):
            densities[i] = 0
        else:
            t = h - hb
            index = np.argmin(t[t >= 0])
            if Lb[index] == 0:
                densities[i] = rho2(h, index)
            else:
                densities[i] = rho1(h, index)

    return densities * 1e3
