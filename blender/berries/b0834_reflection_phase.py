# reflection_phase
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/reflection/reflection.py, line 44
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def reflection_phase(reflectivity):
    """
    Compute the phase of the reflectivity. Returns an array (or float) of
    the phase, in positive multiples of 180 deg or pi rad. So 1 is opposite
    phase. A value of 1.1 would be +1.1 \times \pi rad.

    Args:
        reflectivity (ndarray): The reflectivity, eg from `zoeppritz()`.

    Returns:
        ndarray: The phase, strictly positive
    """
    ph = np.arctan2(np.imag(reflectivity), np.real(reflectivity)) / np.pi
    ph[ph == 1] = 0
    ph[ph < 0] = 2 + ph[ph < 0]
    return ph
