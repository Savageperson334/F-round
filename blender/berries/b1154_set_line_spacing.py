# set_line_spacing
#
# Copied verbatim from https://github.com/benoitguigal/python-epson-printer
#   file epson_printer/epsonprinter.py, line 59
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Thermal printers and obsolete output
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

ESC = 27


def set_line_spacing(dots):
    return [
        ESC,
        51,  # 3
        dots]
