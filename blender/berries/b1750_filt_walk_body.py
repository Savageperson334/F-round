# filt_walk_body
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 2640
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def filt_lcg():
    """24-bit LCG on Y+$1f (cheaper than Park-Miller); new seed sign-extended in B."""
    return '''    move y:(r6+$1f),x0
    move #>$19660d,y0
    mpy x0,y0,a
    asr a
    move a0,a
    add #>$3c6ef3,a
    move a1,y:(r6+$1f)
    move a1,b
'''


def filt_walk_body(tag, stride, lower, bound_reg):
    """One voice's walk step at x:(r1)+; bit 23 of a fresh LCG draw picks the direction.
    Leaves the new position in A1."""
    return filt_lcg()+f'''    tst b
    move #>{stride},b
    move #>{-stride},x0
    tmi x0,b
    move x:(r1),a
    add b,a
    tfr a,b
    add #>10,b
    cmp #>{lower},a
    tlt b,a
    tfr a,b
    sub #>10,b
    cmp {bound_reg},a
    tgt b,a
    move a1,x:(r1)+
'''
