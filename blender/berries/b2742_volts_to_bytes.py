# volts_to_bytes
#
# Copied verbatim from https://github.com/microsoft/SPARROW
#   file sparrow/controller_settings.py, line 130
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def volts_to_bytes(v: float):
    centi = int(round(float(v) / 0.01))
    return [centi & 0xFF, (centi >> 8) & 0xFF]
