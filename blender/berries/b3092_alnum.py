# alnum
#
# Copied verbatim from https://github.com/pkimpel/retro-1620
#   file software/IPL-V/IPL-V-Samples/raven/mkdeck.py, line 51
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def alnum(name, text):                       # alphanumeric data term: PQ=21, <=5 chars in the SYMB field
    s = [" "] * 80; s[48], s[49] = "2", "1"
    for i, c in enumerate(name): s[42 + i] = c
    for i, c in enumerate(text[:5]): s[50 + i] = c
    return "".join(s).rstrip()
