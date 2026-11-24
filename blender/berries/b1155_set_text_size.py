# set_text_size
#
# Copied verbatim from https://github.com/benoitguigal/python-epson-printer
#   file epson_printer/epsonprinter.py, line 66
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Thermal printers and obsolete output
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

GS = 29


def set_text_size(width_magnification, height_magnification):
    if width_magnification < 0 or width_magnification > 7:
        raise Exception("Width magnification should be between 0(x1) and 7(x8)")
    if height_magnification < 0 or height_magnification > 7:
        raise Exception("Height magnification should be between 0(x1) and 7(x8)")
    n = 16 * width_magnification + height_magnification
    byte_array = [
        GS,
        33,   # !
        n]
    return byte_array
