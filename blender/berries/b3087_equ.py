# equ
#
# Copied verbatim from https://github.com/piersfinlayson/rom-bus-control-protocol
#   file reference/host/68k/amiga-boot/tools/mkimage.py, line 209
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

COL = 20


def equ(prefix, suffix, value, comment):
    # A name at or over the column still needs a space before EQU, or the
    # assembler reads the two run together as one identifier.
    name = f"{prefix}_{suffix}"
    line = name + " " * max(1, COL - len(name)) + f"EQU {value}"
    if not comment:
        return line
    return line + " " * max(2, 48 - len(line)) + f"; {comment}"
