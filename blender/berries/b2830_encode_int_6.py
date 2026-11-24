# encode_int_6
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file skywatcher.py, line 404
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def encode_int_6(v: int) -> str:
    '''Encode an integer as 6 hex digits, with the bytes backwards.'''
    h = format(v, '06X')
    assert len(h) == 6, v
    return h[4:6] + h[2:4] + h[0:2]
