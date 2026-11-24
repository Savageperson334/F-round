# sines
#
# Copied verbatim from https://github.com/isod89/clipper-fm1
#   file tools/gen_wavetables.py, line 56
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-pro
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

NH = 128


def sines(amps):
    """amplitudes of sine harmonics 1..NH (missing ones 0) -> spectrum"""
    amps = list(amps) + [0.0] * (NH - len(amps))
    return [(0.0, x) for x in amps[:NH]]
