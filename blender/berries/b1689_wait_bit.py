# wait_bit
#
# Copied verbatim from https://github.com/elpapimango/retroclawd
#   file machines/atari/scenarios/make_scenarios.py, line 32
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def wait_bit(bit, addr):
    """BTST #bit,(addr).W ; BEQ.S back to the BTST: waits until the bit is set."""
    return [0x0838, bit, addr, 0x67F8]
