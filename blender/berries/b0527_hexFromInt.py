# hexFromInt
#
# Copied verbatim from https://github.com/MercuryWorkshop/shipwrecked-pcb
#   file announcement-sender/ellipticcurve/utils/binary.py, line 5
#   licence (as GitHub reports it): Unlicense   see ../licenses/
#   catalogue shelf: Shipwrecks and maritime ghosts
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def hexFromInt(number):
    hexadecimal = "{0:x}".format(number)
    if len(hexadecimal) % 2 == 1:
        hexadecimal = "0" + hexadecimal
    return hexadecimal
