# park_miller_a
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 815
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def park_miller_a(tag):
    """Original 31-bit white-noise sequence, split across Y30/31; output in A."""
    return f'''    ; Multiply the 31-bit seed by 16807 using the full accumulator.
    move y:(r6+$1f),x0
    move #>16807,y0
    mpy x0,y0,a
    move y:(r6+$1e),x0
    mpy x0,y0,b
    asl #16,b,b
    add b,a
    asr a
    move a0,x0
    move a1,x1
    ; Fold the product at bit 31 (modulo 2^31-1).
    asr #7,a,a
    move a1,y1
    move x0,b
    asr #16,b,b
    and #>$ff,b
    move b1,b
    move x1,a
    asl #8,a,a
    and #>$7f00,a
    add b,a
    move a1,y:(r6+$1e)
    move x0,a
    and #>$ffff,a
    add y1,a
    cmp #>$10000,a
    jlt {tag}_noise_no_carry
    sub #>$10000,a
    move y:(r6+$1e),b
    add #>1,b
    move b1,y:(r6+$1e)
{tag}_noise_no_carry:
    move a1,y:(r6+$1f)
    ; Teensy white noise uses the signed low sixteen bits of the new seed.
    asl #8,a,a
    move a1,a
'''
