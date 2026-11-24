# encode_int_2
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file skywatcher.py, line 381
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def encode_int_2(v: int) -> str:
    '''Encode an integer as 2 hex digits.'''
    h = format(v, '02X')
    assert len(h) == 2, v
    return h
