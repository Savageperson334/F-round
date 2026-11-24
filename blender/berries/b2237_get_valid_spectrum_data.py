# get_valid_spectrum_data
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/utility.py, line 1604
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def get_valid_spectrum_data(deltaf, taper_frequencies=[0, 1.0]):
    """extract valid frequency range of spectrum"""
    lower_f, upper_f = taper_frequencies

    lower_idx = int(num.floor(lower_f / deltaf))
    upper_idx = int(num.ceil(upper_f / deltaf))
    return lower_idx, upper_idx
