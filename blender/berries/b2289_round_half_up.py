# round_half_up
#
# Copied verbatim from https://github.com/interactive-sonification/pya
#   file pya/helper/helpers.py, line 208
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import decimal


def round_half_up(number):
    """Round up if >= .5"""
    return int(decimal.Decimal(number).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))
