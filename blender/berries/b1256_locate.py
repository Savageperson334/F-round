# locate
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/c64-rom-reference/scripts/check_bitmap.py, line 16
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def locate(x, y, cia_pins, d018):
    """Ordinary, unscrolled bitmap coordinates in single-dot units."""
    bank = ((~cia_pins) & 3) << 14
    cell = (y // 8) * 40 + x // 8
    bitmap = bank + ((d018 & 8) << 10)
    matrix = bank + ((d018 >> 4) << 10)
    return bitmap + cell * 8 + y % 8, matrix + cell, cell
