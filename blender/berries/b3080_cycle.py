# cycle
#
# Copied verbatim from https://github.com/piersfinlayson/rom-bus-control-protocol
#   file reference/host/68k/amiga-boot/tools/mkball.py, line 212
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

PENS = 8

STEPS = PENS

BANDS_PER_CHECK = PENS // 2


def sphere_colour(band, colours):
    """The colour of a band of longitude on the ball itself, as a $0RGB word.

    Only the band number within one repeat of the pattern matters, which is
    why eight registers can hold the lot.
    """
    return colours[(band % PENS) // BANDS_PER_CHECK]


def cycle(colours):
    """The colour words to write to the ball's registers, one row per step.

    At step s the register holding pen index i shows band i - s, the band the
    ball has turned into that place.  Stepping forward turns the
    front of the ball towards the right of the screen.
    """
    return [[sphere_colour(i - step, colours) for i in range(PENS)]
            for step in range(STEPS)]
