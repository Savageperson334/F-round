# v14enc
#
# Copied verbatim from https://github.com/hunterxiong2026/fm1-felucca-editor-2026
#   file scripts/felucca_link.py, line 238
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def v14enc(v):
    x = v + 8192
    return [x & 0x7F, (x >> 7) & 0x7F]
