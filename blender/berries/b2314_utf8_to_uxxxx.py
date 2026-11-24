# utf8_to_uxxxx
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/textutils.py, line 245
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def utf8_to_uxxxx(in_str, output_array=False):

    char_array = []
    for char in in_str:
        raw_hex = hex(ord(char))[2:].zfill(4).lower()
        char_array.append( "u%s" % raw_hex )

    if output_array:
        return char_array
    else:
        return ' '.join(char_array)
