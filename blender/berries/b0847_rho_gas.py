# rho_gas
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/fluids.py, line 70
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rho_gas(temperature, pressure, molecular_weight):
    """
    Gas density, given temperature (in deg C), pressure (in Pa), and molecular
    weight.

    Args:
        temperature (array): The temperature in degrees Celsius.
        pressure (array): The pressure in pascals.
        molecular_weight (array): The molecular weight.

    Returns:
        array: The density in kg/m3.
    """
    # Align with the symbols and units in Batzle & Wang.
    T, P = np.asanyarray(temperature), np.asanyarray(pressure)*1e-6
    M = np.asanyarray(molecular_weight)
    R = 8.3144598

    return M * P / (R * (T + 273.15))
