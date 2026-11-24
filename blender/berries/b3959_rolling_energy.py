# rolling_energy
#
# Copied verbatim from https://github.com/xaviermouy/ecosound
#   file demo_scripts/extract_pulse_train_features.py, line 21
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def _rolling_energy_1d(x, window, alignment, pad_mode, kernel):
    x2 = x * x


    if alignment == 'center':
        left = window // 2
        right = window - 1 - left
        pad = (left, right)
    elif alignment == 'past':          # causal
        pad = (window - 1, 0)
    else:                               # 'future' anti-causal (lookahead)
        pad = (0, window - 1)


    x2_pad = np.pad(x2, pad, mode=pad_mode)
    # Convolution with 'valid' keeps output length == len(x)
    return np.convolve(x2_pad, kernel, mode='valid')


def rolling_energy(x, window, alignment='center', pad_mode='reflect'):
    """
    Rolling energy (sum of squares) over a window along the last axis.


    Args:
        x (array-like): 1D waveform (or ND, time on the last axis).
        window (int): number of samples in the window (>=1).
        alignment (str):
            - 'center': centered window (default)
            - 'past'  : causal; includes current and previous (window-1) samples
            - 'future': anti-causal; includes current and next (window-1) samples
        pad_mode (str): np.pad mode for edge handling ('reflect', 'edge', 'constant', ...)


    Returns:
        np.ndarray: same shape as x with rolling energy along the last axis.
    """
    if window < 1:
        raise ValueError("window must be >= 1")
    if alignment not in ('center', 'past', 'future'):
        raise ValueError("alignment must be 'center', 'past', or 'future'")


    x = np.asarray(x, dtype=np.float64)
    kernel = np.ones(int(window), dtype=np.float64)


    # Handle multi-d arrays by applying along the last axis
    if x.ndim > 1:
        return np.apply_along_axis(
            lambda v: _rolling_energy_1d(v, window, alignment, pad_mode, kernel),
            axis=-1, arr=x
        )
    else:
        return _rolling_energy_1d(x, window, alignment, pad_mode, kernel)
