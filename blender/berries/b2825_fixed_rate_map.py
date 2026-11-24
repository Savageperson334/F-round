# fixed_rate_map
#
# Copied verbatim from https://github.com/nforrester/NexPlane
#   file nexstar.py, line 85
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

SIDERIAL_RATE_RADIANS_PER_SECOND = 7.2921150e-5


def fixed_rate_map(fixed_rate: int) -> int:
    '''The telescope has several fixed slew rates you can invoke.
    Given a fixed rate index, return the corresponding rate in quarter arcseconds per second.'''
    siderial_rate = int(SIDERIAL_RATE_RADIANS_PER_SECOND / math.pi * 180 * 60 * 60 * 4)
    degree_per_second = 60 * 60 * 4
    if fixed_rate == 0:
        return 0
    if fixed_rate == 1:
        return int(0.5 * siderial_rate)
    if fixed_rate == 2:
        return 1 * siderial_rate
    if fixed_rate == 3:
        return 4 * siderial_rate
    if fixed_rate == 4:
        return 8 * siderial_rate
    if fixed_rate == 5:
        return 16 * siderial_rate
    if fixed_rate == 6:
        return 64 * siderial_rate
    if fixed_rate == 7:
        return 1 * degree_per_second
    if fixed_rate == 8:
        return 3 * degree_per_second
    if fixed_rate == 9:
        return 5 * degree_per_second
    raise Exception(f'Bad fixed rate: {fixed_rate}')
