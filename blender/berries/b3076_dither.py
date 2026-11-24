# dither
#
# Copied verbatim from https://github.com/piersfinlayson/rom-bus-control-protocol
#   file reference/host/6502/c64-led-test/tools/gen_disc.py, line 36
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def dither(threshold):
    return tuple(
        sum(1 << (7 - px) for px in range(8) if BAYER[py % 4][px % 4] < threshold)
        for py in range(8)
    )
