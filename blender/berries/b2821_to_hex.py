# to_hex
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file nexstar.py, line 66
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_hex(num_digits: int, value: int) -> str:
    '''Convert an int to a hexadecimal string, with enough leading zeros so that it has exactly the specified number of digits.'''
    assert value < 16**num_digits
    return '%0*X' % (num_digits, value)
