# fb_fm_const
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 1842
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fb_fm_const(mantissa, shift):
    # a = min(x1, (x0*mantissa)<<shift); shift<=7 cannot overflow A.
    assert shift<=7
    s=f'    move #>${mantissa:x},y0\n    mpy x0,y0,a\n'
    if shift: s+=f'    asl #{shift},a,a\n'
    return s+'    cmp x1,a\n    tgt x1,a\n'
