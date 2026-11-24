# compose_chinese_string_v3
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/textutils.py, line 142
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

chinese_compose_map_v3 = dict()


def compose_chinese_char_v3(decomposed_char):
    #print("Called for: [%s]" % decomposed_char)
    if decomposed_char not in chinese_compose_map_v3:
        raise Exception("Shouldn't get here...")
        # return something!
        #if len(decomposed_char) > 1:
        #    return decomposed_char[1]
        #else:
        #    return decomposed_char[0]

    return chinese_compose_map_v3[decomposed_char]


def compose_chinese_string_v3(decomposed_string):
    # First pass-- let's assume we have a well-formed string
    cur_idx = 0
    out_str = ''
    while cur_idx < len(decomposed_string):
        composition_type = decomposed_string[cur_idx]

        if composition_type in ['一', '品', '叕', '吅', '吕', '回', '咒', '弼', '冖', '˖']:
            # Usually have 3 chars to consume (composition type, part1, part2)
            # But may need to handle a v0/v1/v2 subscript
            nchars = 3
            if (cur_idx + 3 < len(decomposed_string)) and (decomposed_string[cur_idx + 3] in ['\ue001','\ue002','\ue003']):
                nchars = 4

            decomposed_char = decomposed_string[cur_idx : cur_idx + nchars]
            out_str += compose_chinese_char_v3(decomposed_char)
            cur_idx += nchars
        else:
            # We don't have a match; possibly the char was not decomposable; possibly error in parsing
            # For now, just append char and move to the next spot
            out_str += decomposed_string[cur_idx]
            cur_idx += 1


    return out_str
