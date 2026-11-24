# compose_chinese_string
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/textutils.py, line 71
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


def compose_chinese_string(decomposed_string):
    # First pass-- let's assume we have a well-formed string
    cur_idx = 0
    out_str = ''
    while cur_idx < len(decomposed_string):
        composition_type = decomposed_string[cur_idx]
        if composition_type == '一' or composition_type == '品' or composition_type == '叕':
            # only have a single-part composition
            # But may need to handle a v0/v1/v2 subscript
            nchars = 2
            if (cur_idx + 2 < len(decomposed_string)) and (decomposed_string[cur_idx + 2] == '₀' or decomposed_string[cur_idx + 2] == '₁' or decomposed_string[cur_idx + 2] == '₂'):
                nchars = 3

            decomposed_char = decomposed_string[cur_idx : cur_idx + nchars]
            out_str += compose_chinese_char(decomposed_char)
            cur_idx += nchars
        elif composition_type == '吅' or composition_type == '吕' or composition_type == '回' or composition_type == '咒' or composition_type == '弼' or composition_type == '冖' or composition_type == '˖':
            # here we have two-part composition
            # Need to handle: do we have a v0/v1/v2 subscript
            nchars = 3
            if (cur_idx + 3 < len(decomposed_string)) and (decomposed_string[cur_idx + 3] == '₀' or decomposed_string[cur_idx + 3] == '₁' or decomposed_string[cur_idx + 3] == '₂'):
                nchars = 4

            decomposed_char = decomposed_string[cur_idx : cur_idx + nchars]
            out_str += compose_chinese_char(decomposed_char)
            cur_idx += nchars
        else:
            # We don't have a match; possibly the char was not decomposable; possibly error in parsing
            # For now, just append char and move to the next spot
            out_str += decomposed_string[cur_idx]
            cur_idx += 1


    return out_str
