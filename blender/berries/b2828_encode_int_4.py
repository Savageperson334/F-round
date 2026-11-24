# encode_int_4
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file skywatcher.py, line 392
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def encode_int_4(v: int) -> str:
    '''Encode an integer as 4 hex digits, with the bytes backwards.'''
    h = format(v, '04X')
    assert len(h) == 4, v
    return h[2:4] + h[0:2]
