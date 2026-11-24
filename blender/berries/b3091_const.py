# const
#
# Copied verbatim from https://github.com/pkimpel/retro-1620
#   file software/IPL-V/IPL-V-Samples/raven/mkdeck.py, line 19
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def const(comment, name, value):            # integer data term, value right-justified to col 61
    s = [" "] * 80
    comment = re.sub(r"[^A-Z0-9.)*$(,=@+\-/ ]", " ", comment.upper())
    for i, c in enumerate(comment[:34]): s[6 + i] = c
    s[42], s[43], s[48], s[49] = name[0], name[1], "0", "1"
    v = str(value)
    for i, c in enumerate(v): s[61 - len(v) + i] = c
    return "".join(s).rstrip()
