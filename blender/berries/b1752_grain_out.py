# grain_out
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 3257
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def grain_out(mode):
    """Grain in X1, oscillator in B -> one output sample."""
    if mode==0:
        return '''    move b1,x0
    move x1,a
    or x0,a
    asl #8,a,a
    move a1,y:(r7)+
'''
    if mode==1:
        # Original gain 32000 on a sixteen-bit grain clips every nonzero sample to (nearly) full
        # scale; saturate in two steps, as a shift of 23 would overflow the guard bits.
        return '''    move x1,a
    asl #16,a,a
    move a,x0
    move x0,a
    asl #7,a,a
    move a,x0
    move y:(r6+$25),y0
    mpy x0,y0,a
    move y:(r6+$21),x0
    mac -x0,y0,a
    add x0,a
    move a,y:(r6+$21)
    move a,y:(r7)+
'''
    return '''    move x1,a
    asl #8,a,a
    move a1,y:(r7)+
'''
