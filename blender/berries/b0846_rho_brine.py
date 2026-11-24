# rho_brine
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/fluids.py, line 42
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rho_water(temperature, pressure):
    """
    The density of pure water, as a function of temperature and pressure.
    Implements equation 27a from Batzle and Wang (1992).

    Use scalars or arrays; if you use arrays, they must be the same size.

    Args:
        temperature (array): The temperature in degrees Celsius.
        pressure (array): The pressure in pascals.

    Returns:
        array: The density in kg/m3.
    """
    # Align with the symbols and units in Batzle & Wang.
    T, P = np.asanyarray(temperature), np.asanyarray(pressure)*1e-6

    x = -80*T - 3.3*T**2 + 0.00175*T**3 + 489*P - 2*T*P \
        + 0.016*P*T**2 - 1.3e-5*P*T**3 - 0.333*P**2 - 0.002*T*P**2

    return 1000 + 1e-3 * x


def rho_brine(temperature, pressure, salinity):
    """
    The density of NaCl brine, given temperature, pressure, and salinity.
    The density of pure water is computed from rho_water(). Implements
    equation 27b from Batzle and Wang (1992).

    Use scalars or arrays; if you use arrays, they must be the same size.

    Args:
        temperature (array): The temperature in degrees Celsius.
        pressure (array): The pressure in pascals.
        salinity (array): The weight fraction of NaCl, e.g. 35e-3
            for 35 parts per thousand, or 3.5% (the salinity of
            seawater).

    Returns:
        array: The density in kg/m3.
    """
    # Align with the symbols and units in Batzle & Wang.
    T, P = np.asanyarray(temperature), np.asanyarray(pressure)*1e-6
    S = np.asanyarray(salinity)

    rho_w = rho_water(temperature, pressure) / 1000
    x = 300*P - 2400*P*S + T*(80 + 3*T - 3300*S - 13*P + 47*P*S)

    return rho_w + S*(0.668 + 0.44*S + 1e-6 * x)
