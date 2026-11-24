# s16
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/genesis.py, line 38
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def s16(x):
    x &= 0xFFFF
    return x - (1 << 16) if x & 0x8000 else x
