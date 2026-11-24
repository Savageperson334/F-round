# sound_speed_chen_millero
#
# Copied verbatim from https://github.com/GalaxyUrsa/Pisces-Explorer
#   file backend/data.py, line 13
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ocean currents and fluid dynamics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def sound_speed_chen_millero(T, S, z):
    """UNESCO / Chen-Millero (1977) sound speed formula."""
    P = z * 0.1  # dbar
    Cw = (
        (1402.388
         + 5.03830 * T - 5.81090e-2 * T**2 + 3.3432e-4 * T**3
         - 1.47797e-6 * T**4 + 3.1419e-9 * T**5)
        + P * (0.153563 + 6.8999e-4 * T - 8.1829e-6 * T**2
               + 1.3632e-7 * T**3 - 6.1260e-10 * T**4)
        + P**2 * (3.1260e-5 - 1.7111e-6 * T + 2.5986e-8 * T**2
                  - 2.5353e-10 * T**3 + 1.0415e-12 * T**4)
        + P**3 * (-9.7729e-9 + 3.8513e-10 * T - 2.3654e-12 * T**2)
    )
    A = (
        (1.389 - 1.262e-2 * T + 7.166e-5 * T**2
         + 2.008e-6 * T**3 - 3.21e-8 * T**4)
        + P * (9.4742e-5 - 1.2583e-5 * T - 6.4928e-8 * T**2
               + 1.0515e-8 * T**3 - 2.0142e-10 * T**4)
        + P**2 * (-3.9064e-7 + 9.1061e-9 * T - 1.6009e-10 * T**2
                  + 7.994e-12 * T**3)
        + P**3 * (1.100e-10 + 6.651e-12 * T - 3.391e-13 * T**2)
    )
    B = -1.922e-2 - 4.42e-5 * T + P * 7.3637e-5 + P * T * 1.7950e-7
    D = 1.727e-3 - 7.9836e-6 * P
    S_nn = np.where(S >= 0, S, np.nan)  # S**1.5 is undefined for negative S
    return Cw + A * S_nn + B * S_nn**1.5 + D * S_nn**2
