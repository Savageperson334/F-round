# key_name
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/velo_capture.py, line 25
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def key_name(k):
    m = 53 + k
    return f"{NAMES[m % 12]}{m // 12 - 1}"
