# bits_and_bytes
#
# Copied verbatim from https://github.com/magicshifter/ms4000
#   file tools/esptool/ecdsa/util.py, line 98
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def bits_and_bytes(order):
    bits = int(math.log(order-1, 2)+1)
    bytes = bits // 8
    extrabits = bits % 8
    return bits, bytes, extrabits
