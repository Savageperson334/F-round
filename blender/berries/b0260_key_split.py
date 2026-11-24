# key_split
#
# Copied verbatim from https://github.com/GRiMMBIENT/grimm
#   file tools/sampleio.py, line 329
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: genkigenki/Speak37, isod89/clipper-fm1, isod89/clipper-pro, jbschooley/Virtual-FM-1, kpalaniuk/gnomad-firmware, oscillr/LRRY
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def key_split(roots):
    """sorted root notes -> [(lo, hi)]: each zone reaches halfway to its neighbours, the
    outer zones to the ends of the keyboard"""
    n = len(roots)
    return [(0 if j == 0 else (roots[j - 1] + r) // 2 + 1, 127 if j == n - 1 else (r + roots[j + 1]) // 2)
            for j, r in enumerate(roots)]
