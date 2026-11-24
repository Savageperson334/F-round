# sonify
#
# Copied verbatim from https://github.com/BeatKitchen/Beat-Kitchen-Weather-Sonification
#   file sonify.py, line 77
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def sonify(data, sample_rate):
    """
    Convert a numeric array to 16-bit PCM audio.

    Steps:
      1. Subtract the mean (remove DC offset)
         - For barometric pressure (~1013 mb), this centers the signal
           at zero so the fluctuations become the audible waveform
      2. Normalize to the range [-1.0, 1.0]
         - Scales the largest deviation to full amplitude
      3. Convert to 16-bit signed integers for WAV output
    """
    # Step 1: Remove DC offset
    centered = data - np.mean(data)

    # Step 2: Normalize to [-1.0, 1.0]
    peak = np.max(np.abs(centered))
    if peak > 0:
        normalized = centered / peak
    else:
        normalized = centered

    # Step 3: Convert to 16-bit PCM
    audio = (normalized * 32767).astype(np.int16)

    return audio
