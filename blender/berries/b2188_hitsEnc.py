# hitsEnc
#
# Copied verbatim from https://github.com/hunterxiong2026/fm1-felucca-editor-2026
#   file scripts/felucca_link.py, line 247
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def hitsEnc(hit, acc):
    hi = ((hit >> 7) & 1) | (((acc >> 7) & 1) << 1)
    return [hit & 0x7F, acc & 0x7F, hi]
