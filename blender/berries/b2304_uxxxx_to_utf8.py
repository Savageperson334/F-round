# uxxxx_to_utf8
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/remove_ascii.py, line 10
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def uxxxx_to_utf8(in_char):
    # First get the 'xxxx' part out of the current 'uxxxx' char
    char = in_char[1:]
    # Now decode the hex code point into utf-8
    utf8_char = chr(int(char, 16))
    return utf8_char
