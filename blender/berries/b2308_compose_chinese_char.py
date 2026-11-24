# compose_chinese_char
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/textutils.py, line 50
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

chinese_compose_map = dict()


def compose_chinese_char(decomposed_char):
    #print("Called for: [%s]" % decomposed_char)
    if decomposed_char not in chinese_compose_map:
        #raise Exception("Shouldn't get here...")
        # return something!
        if len(decomposed_char) > 1:
            return decomposed_char[1]
        else:
            return decomposed_char[0]

    return chinese_compose_map[decomposed_char]
