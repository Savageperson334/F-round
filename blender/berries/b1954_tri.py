# tri
#
# Copied verbatim from https://github.com/genkigenki/Speak37
#   file tools/uac_tone_check.py, line 16
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: oscillr/LRRY
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def tri(ph):
    q = ph if ph < 50 else 100 - ph
    return q * 1000 - 25000, abs(50 - ph) * 1000 - 25000
