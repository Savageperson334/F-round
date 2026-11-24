# tighten_signal_limits_peak
#
# Copied verbatim from https://github.com/xaviermouy/ecosound
#   file ecosound/core/tools.py, line 192
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def tighten_signal_limits_peak(signal, percentage_max_energy):
    """
    Tighten signal limits based on peak energy samples.

    Redefines the start and stop sample indices by identifying the smallest
    contiguous window that contains the highest-energy samples, representing
    ``percentage_max_energy`` percent of the total signal energy. Samples are
    ranked by energy (highest first) rather than by position. Smaller values of
    ``percentage_max_energy`` produce a tighter (shorter) window.

    Parameters
    ----------
    signal : numpy.ndarray
        1-D waveform array.
    percentage_max_energy : float
        Percentage of total signal energy to capture (0–100). Smaller values
        yield tighter windows around the most energetic part of the signal.

    Returns
    -------
    chunk : list of int
        Two-element list ``[start_sample, stop_sample]`` spanning the window
        that contains the requested percentage of peak energy.

    """
    squared_signal = np.square(signal)
    norm_factor = sum(squared_signal)
    squared_signal_normalized = squared_signal / norm_factor
    sort_idx = np.argsort(-squared_signal_normalized)
    sort_val = squared_signal_normalized[sort_idx]
    sort_val_cum = np.cumsum(sort_val)
    id_limit = np.where(sort_val_cum > (percentage_max_energy / 100))
    id_limit = id_limit[0][0]
    min_idx_limit = np.min(sort_idx[0:id_limit])
    max_idx_limit = np.max(sort_idx[0:id_limit])
    chunk = [min_idx_limit, max_idx_limit]

    return chunk
