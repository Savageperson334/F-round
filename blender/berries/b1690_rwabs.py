# rwabs
#
# Copied verbatim from https://github.com/elpapimango/retroclawd
#   file machines/atari/scenarios/make_scenarios.py, line 131
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def rwabs(rwflag, buf):
    return [
        0x3F3C, 0x0000,          # MOVE.W #0,-(SP)        dev A
        0x3F3C, 0x001E,          # MOVE.W #30,-(SP)       recno
        0x3F3C, 0x0001,          # MOVE.W #1,-(SP)        cnt
        0x2F3C, buf >> 16, buf & 0xFFFF,  # MOVE.L #buf,-(SP)
        0x3F3C, rwflag,          # MOVE.W #rwflag,-(SP)
        0x3F3C, 0x0004,          # MOVE.W #4,-(SP)        Rwabs
        0x4E4D,                  # TRAP #13
        0xDFFC, 0x0000, 0x000E,  # ADDA.L #14,SP
    ]
