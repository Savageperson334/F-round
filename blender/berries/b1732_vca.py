# vca
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/effects/ladder/make_tables.py, line 74
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

TEMPO = 2880


def vca(k):             # VCA: 127 bypass (0), 64-126 envelope (1), 0-63 gate samples
    if k == 127:
        return 0
    if k >= 64:
        return 1
    return max(2, ((((k + 1) * 128) * 44100) >> 10) * 360 // TEMPO)
