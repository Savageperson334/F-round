# base_len
#
# Copied verbatim from https://github.com/LaM3rzLG/FreeTVC
#   file tools/re/z80trace.py, line 15
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def base_len(op):
    if op in (0x01, 0x11, 0x21, 0x31, 0x22, 0x2A, 0x32, 0x3A, 0xC3, 0xCD) or op & 0xC7 in (0xC2, 0xC4):
        return 3
    if op & 0xC7 in (0x06, 0xC6) or op in (0x10, 0x18, 0x20, 0x28, 0x30, 0x38, 0xD3, 0xDB, 0xCB):
        return 2
    return 1
