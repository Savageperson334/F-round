# norm
#
# Copied verbatim from https://github.com/genkigenki/Speak37
#   file tools/gen_waves.py, line 33
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-fm1, isod89/clipper-pro, jbschooley/Virtual-FM-1, kpalaniuk/gnomad-firmware
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def norm(s, peak=30000):
    m = max(1e-9, max(abs(v) for v in s))
    return [v * peak / m for v in s]
