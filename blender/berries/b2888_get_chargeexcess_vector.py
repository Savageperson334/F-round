# get_chargeexcess_vector
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 445
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def spherical_to_cartesian(zenith, azimuth):
    sinZenith = np.sin(zenith)
    x = sinZenith * np.cos(azimuth)
    y = sinZenith * np.sin(azimuth)
    z = np.cos(zenith)

    if hasattr(zenith, '__len__') and hasattr(azimuth, '__len__'):
        return np.array([x, y, z]).T
    else:
        return np.array([x, y, z])


def get_chargeexcess_vector(core, zenith, azimuth, stationPosition):
    showerAxis = spherical_to_cartesian(zenith, azimuth)
    magnitues = np.dot((stationPosition - core), showerAxis)
    showerAxis = np.outer(magnitues, showerAxis)
    chargeExcessVector = core - stationPosition + showerAxis
    norm = np.linalg.norm(chargeExcessVector.T, axis=0)
    chargeExcessVector = (chargeExcessVector.T / norm).T
    return np.squeeze(chargeExcessVector)
