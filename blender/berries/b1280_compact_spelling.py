# compact_spelling
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/pcode-disassembly/scripts/reconstruct/dtl_fn_reading.py, line 11
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def compact_spelling(text):
    """Exact lexical comparison apart from ASCII spaces outside string literals."""
    quoted = False
    output = []
    for char in text:
        if char == '"':
            quoted = not quoted
        if char != ' ' or quoted:
            output.append(char)
    return None if quoted else ''.join(output)
