# smoothstep
#
# Copied verbatim from https://github.com/jessemelpolio/non-stationary_texture_syn
#   file util/perlin2d.py, line 13
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Textures and materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def smoothstep(t):
    """Smooth curve with a zero derivative at 0 and 1, making it useful for
    interpolating.
    """
    return t * t * (3. - 2. * t)
