# rgb
#
# Copied verbatim from https://github.com/piersfinlayson/rom-bus-control-protocol
#   file reference/host/68k/amiga-boot/tools/mkball.py, line 371
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def rgb(word):
    """A 12-bit $0RGB word as the eight-bit triple a PNG wants."""
    return (((word >> 8) & 0xF) * 0x11,
            ((word >> 4) & 0xF) * 0x11,
            (word & 0xF) * 0x11)
