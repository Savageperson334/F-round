# v_water
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/fluids.py, line 91
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def v_water(temperature, pressure):
    """
    The acoustic velocity of pure water, as a function of temperature
    and pressure. Implements equation 28 from Batzle and Wang (1992), using
    the coefficients in Table 1.

    Note that this function does not work at pressures above about 100 MPa.

    Use scalars or arrays; if you use arrays, they must be the same size.

    Args:
        temperature (array): The temperature in degrees Celsius.
        pressure (array): The pressure in pascals.

    Returns:
        array: The velocity in m/s.
    """
    w = np.array([[ 1.40285e+03,  1.52400e+00,  3.43700e-03, -1.19700e-05],
                  [ 4.87100e+00, -1.11000e-02,  1.73900e-04, -1.62800e-06],
                  [-4.78300e-02,  2.74700e-04, -2.13500e-06,  1.23700e-08],
                  [ 1.48700e-04, -6.50300e-07, -1.45500e-08,  1.32700e-10],
                  [-2.19700e-07,  7.98700e-10,  5.23000e-11, -4.61400e-13]])

    T, P = np.asanyarray(temperature), np.asanyarray(pressure) * 1e-6
    return sum(w[i, j] * T**i * P**j for i in range(5) for j in range(4))
