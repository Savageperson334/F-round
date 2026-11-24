# hitsDec
#
# Copied verbatim from https://github.com/hunterxiong2026/fm1-felucca-editor-2026
#   file scripts/felucca_link.py, line 252
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def hitsDec(h, c, x):
    hit = h | ((x & 1) << 7)
    acc = (c | ((x & 2) << 6)) & hit
    return hit, acc
