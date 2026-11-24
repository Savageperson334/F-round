# decompose_chinese_char_v3
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/textutils.py, line 109
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

chinese_decompose_map = dict()

chinese_decompose_map_v3 = dict()

filler_space = '\ue000'


def decompose_chinese_char_v3(char):
    if char not in chinese_decompose_map_v3:
        return filler_space + char + filler_space
    dseq = chinese_decompose_map[char]
    return ''.join(dseq)
