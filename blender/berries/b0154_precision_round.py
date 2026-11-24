# precision_round
#
# Copied verbatim from https://github.com/DirtBurner/GeoChem_Class
#   file neuhaus_fcns.py, line 263
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def precision_round(number, digits=3):
    '''
    Rounds scientific notation numbers to number of digits. Courtesy of Josh Duran, Stack Overflow, 16 Dec 2020
    '''
    power = "{:e}".format(number).split('e')[1]
    return round(number, -(int(power) - digits))
