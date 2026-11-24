# setup
#
# Copied verbatim from https://github.com/elpapimango/retroclawd
#   file machines/atari/timing/gen_p29.py, line 91
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def setup(base, end, mode, control):
    """Stop, program the frame and the mode, start with `control` in $FF8901."""
    out = ["    clr.b   $01(a3)"]
    out += [
        f"    move.b  #${(base >> 16) & 0xFF:02x},$03(a3)",
        f"    move.b  #${(base >> 8) & 0xFF:02x},$05(a3)",
        f"    move.b  #${base & 0xFF:02x},$07(a3)",
        f"    move.b  #${(end >> 16) & 0xFF:02x},$0f(a3)",
        f"    move.b  #${(end >> 8) & 0xFF:02x},$11(a3)",
        f"    move.b  #${end & 0xFF:02x},$13(a3)",
        f"    move.b  #${mode:02x},$21(a3)",
        f"    move.b  #${control:02x},$01(a3)",
    ]
    return out
