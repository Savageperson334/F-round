# from_hex
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file nexstar.py, line 71
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def from_hex(hex_text: str) -> int:
    '''Convert a hexadecimal string to an integer.'''
    return int(hex_text, 16)
