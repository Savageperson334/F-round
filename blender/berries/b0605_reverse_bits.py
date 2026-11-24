# reverse_bits
#
# Copied verbatim from https://github.com/NaitLee/Cat-Printer
#   file printer_lib/commander.py, line 42
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Thermal printers and obsolete output
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def reverse_bits(i: int):
    'Reverse the bits of this byte (as `int`)'
    i = ((i & 0b10101010) >> 1) | ((i & 0b01010101) << 1)
    i = ((i & 0b11001100) >> 2) | ((i & 0b00110011) << 2)
    return ((i & 0b11110000) >> 4) | ((i & 0b00001111) << 4)
