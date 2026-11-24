# append_PKCS7_padding
#
# Copied verbatim from https://github.com/magicshifter/ms4000
#   file tools/esptool/pyaes/util.py, line 47
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_bufferable(binary):
    return binary


def append_PKCS7_padding(data):
    pad = 16 - (len(data) % 16)
    return data + to_bufferable(chr(pad) * pad)
