# b24_to_hex8
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file nexstar.py, line 79
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


def wrap_b24(theta: int, minimum: int) -> int:
    '''Wrap an angle expressed in units of 1/(2**24) turns into the range minimum to (minimum + 2**24).'''
    while theta >= minimum + 2**24:
        theta -= 2**24
    while theta < minimum:
        theta += 2**24
    return theta


def b24_to_hex8(b24: int) -> str:
    '''Convert a 24 bit angle to an 8 digit hex string (the two least significant digits get set to zero).'''
    return to_hex(8, wrap_b24(b24, 0) << 8)
