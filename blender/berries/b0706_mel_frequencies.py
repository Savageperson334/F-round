# mel_frequencies
#
# Copied verbatim from https://github.com/Scottcjn/naturelm-cats
#   file NatureLM/utils.py, line 85
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def mel_frequencies(n_mels, fmin, fmax):
    def _hz_to_mel(f):
        return 2595 * np.log10(1 + f / 700)

    def _mel_to_hz(m):
        return 700 * (10 ** (m / 2595) - 1)

    low = _hz_to_mel(fmin)
    high = _hz_to_mel(fmax)

    mels = np.linspace(low, high, n_mels)

    return _mel_to_hz(mels)
