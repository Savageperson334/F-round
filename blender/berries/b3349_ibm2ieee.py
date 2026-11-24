# ibm2ieee
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/io/segy.py, line 18
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ibm2ieee(ibm):
    """
    Converts an IBM floating point number into IEEE format.
    :param: ibm - 32 bit unsigned integer: unpack('>L', f.read(4))
    """
    if ibm == 0:
        return 0.0
    sign = ibm >> 31 & 0x01
    exponent = ibm >> 24 & 0x7f
    mantissa = (ibm & 0x00ffffff) / float(pow(2, 24))
    print('x', sign, exponent - 64, mantissa)
    return (1 - 2 * sign) * mantissa * float(pow(16, exponent - 64))
