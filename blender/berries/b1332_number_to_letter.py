# number_to_letter
#
# Copied verbatim from https://github.com/cbassa/stvid
#   file process.py, line 33
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def number_to_letter(n):
    # 
    if n == 0:
        return ""
    x = (n - 1) % 24
    letters = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    rest = (n - 1) // 24
    if rest == 0:
        return letters[x]
    return number_to_letter(rest) + letters[x]
