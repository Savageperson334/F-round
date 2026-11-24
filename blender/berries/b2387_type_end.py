# type_end
#
# Copied verbatim from https://github.com/jbschooley/Virtual-FM-1
#   file engines/felucca/fel_state.py, line 68
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def type_end(body):
    """the index just past the type at the start of body (up to a space outside brackets and strings)"""
    depth, quoted = 0, False
    for i, c in enumerate(body):
        if c == '"':
            quoted = not quoted
        elif quoted:
            continue
        elif c in '[{<(':
            depth += 1
        elif c in ']}>)':
            depth -= 1
        elif c == ' ' and depth == 0:
            return i
    return len(body)
