# next_power_of_2
#
# Copied verbatim from https://github.com/xaviermouy/ecosound
#   file ecosound/core/spectrogram.py, line 606
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def next_power_of_2(x):
    """Calculate the next power of two for x."""
    return 1 if x == 0 else 2 ** (x - 1).bit_length()
