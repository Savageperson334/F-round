# move_b
#
# Copied verbatim from https://github.com/elpapimango/retroclawd
#   file machines/atari/scenarios/make_scenarios.py, line 13
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def move_b(value, addr):
    """MOVE.B #value,(addr).W"""
    return [0x11FC, value, addr]
