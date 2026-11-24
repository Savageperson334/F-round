# kiss_escape
#
# Copied verbatim from https://github.com/daniestevez/gr-satellites
#   file python/kiss.py, line 20
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy

FEND = numpy.uint8(0xc0)

FESC = numpy.uint8(0xdb)

TFEND = numpy.uint8(0xdc)

TFESC = numpy.uint8(0xdd)


def kiss_escape(a):
    """Escapes KISS control characters

    This replaces FEND and FESC according to the KISS escape rules
    """
    buff = list()
    for x in a:
        if x == FESC:
            buff.append(FESC)
            buff.append(TFESC)
        elif x == FEND:
            buff.append(FESC)
            buff.append(TFEND)
        else:
            buff.append(numpy.uint8(x))
    return buff
