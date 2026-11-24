# screen_char
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file shared/6502/data-classify6502.py, line 7
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def screen_char(b):
    if b == 0x20: return ' '
    if 1 <= b <= 26: return chr(64 + b)
    if 0x30 <= b <= 0x39: return chr(b)
    return None
