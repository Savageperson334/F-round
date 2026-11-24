# decompose_chinese_string
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/textutils.py, line 44
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

chinese_decompose_map = dict()


def decompose_chinese_char(char):
    if char not in chinese_decompose_map:
        return char
    dseq = chinese_decompose_map[char]
    return ''.join(dseq)


def decompose_chinese_string(string):
    out_str = ''
    for char in string:
        out_str += decompose_chinese_char(char)
    return out_str
