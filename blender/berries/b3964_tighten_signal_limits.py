# tighten_signal_limits
#
# Copied verbatim from https://github.com/xaviermouy/ecosound
#   file ecosound/core/tools.py, line 158
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def tighten_signal_limits(signal, energy_percentage):
    """
    Tighten signal limits based on cumulative energy.

    Redefines the start and stop sample indices to retain the central
    ``energy_percentage`` percent of the signal's cumulative energy. Equal
    amounts of energy are trimmed from both ends.

    Parameters
    ----------
    signal : numpy.ndarray
        1-D waveform array.
    energy_percentage : float
        Percentage of the total signal energy to retain (0–100). Higher values
        keep more of the signal; lower values crop more aggressively.

    Returns
    -------
    chunk : list of int
        Two-element list ``[start_sample, stop_sample]`` with the new sample
        indices bounding the requested energy percentage.

    """
    cumul_energy = np.cumsum(np.square(signal))
    cumul_energy = cumul_energy / max(cumul_energy)
    percentage_begining = (1 - (energy_percentage / 100)) / 2
    percentage_end = 1 - percentage_begining
    chunk = [
        np.nonzero(cumul_energy > percentage_begining)[0][0],
        np.nonzero(cumul_energy > percentage_end)[0][0],
    ]
    return chunk
