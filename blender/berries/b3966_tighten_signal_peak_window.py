# tighten_signal_peak_window
#
# Copied verbatim from https://github.com/xaviermouy/ecosound
#   file ecosound/core/tools.py, line 232
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def tighten_signal_peak_window(signal, fs, half_width_sec):
    """
    Tighten signal limits using a fixed-width window centred on the energy peak.

    Finds the sample with the maximum instantaneous energy (squared amplitude)
    and returns a symmetric window of ``±half_width_sec`` seconds around it.
    The window is clamped to the signal boundaries if it would extend beyond them.

    Parameters
    ----------
    signal : numpy.ndarray
        1-D waveform array.
    fs : float
        Sampling frequency in Hz.
    half_width_sec : float
        Half-width of the window in seconds. The total window duration is
        ``2 * half_width_sec``.

    Returns
    -------
    chunk : list of int
        Two-element list ``[start_sample, stop_sample]``.
    """
    peak_idx = int(np.argmax(np.square(signal)))
    half_samples = int(round(half_width_sec * fs))
    start = max(0, peak_idx - half_samples)
    stop  = min(len(signal) - 1, peak_idx + half_samples)
    return [start, stop]
