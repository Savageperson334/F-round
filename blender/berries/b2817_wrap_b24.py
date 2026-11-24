# wrap_b24
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file nexstar.py, line 40
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def wrap_b24(theta: int, minimum: int) -> int:
    '''Wrap an angle expressed in units of 1/(2**24) turns into the range minimum to (minimum + 2**24).'''
    while theta >= minimum + 2**24:
        theta -= 2**24
    while theta < minimum:
        theta += 2**24
    return theta
