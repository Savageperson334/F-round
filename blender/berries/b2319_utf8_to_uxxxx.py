# utf8_to_uxxxx
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/trans_to_uxxxx.py, line 5
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def utf8_to_uxxxx(in_str):

    char_array = []
    out_str = ""
    for char in in_str:
        if char == " ":
            out_str += '_'.join(char_array) + " "
            char_array = []
        else:
            raw_hex = hex(ord(char))[2:].zfill(4).lower()
            char_array.append( "u%s" % raw_hex )

    if len(char_array) > 0:
        out_str += '_'.join(char_array)

    return out_str
