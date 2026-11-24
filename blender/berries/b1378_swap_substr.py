# swap_substr
#
# Copied verbatim from https://github.com/citiesskylines-csur/CSUR
#   file prefab/prop_utils.py, line 29
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def swap_substr(s, one, other):
    s = s.replace(one, "$$SUBSTR1$$").replace(other, "$$SUBSTR2$$")
    s = s.replace("$$SUBSTR1$$", other).replace("$$SUBSTR2$$", one)
    return s
