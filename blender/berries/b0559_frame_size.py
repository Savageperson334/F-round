# frame_size
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/genesis.py, line 87
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

BYTES_UTILES = [2, 31, 17, 41, 35, 27, 135, 45, 31, 123, 251, 37, 64, 249, 38, 73]

BYTES_UTILES_L = [2, 31, 17, 41, 35, 27, 1, 23, 31, 123, 251, 37, 64, 249, 38, 101]

SIZES_BY_SOURCE = {3: BYTES_UTILES, 5: BYTES_UTILES_L}


def frame_size(source, ptype):
    table = SIZES_BY_SOURCE.get(source, BYTES_UTILES)
    return table[ptype] if ptype < len(table) else None
