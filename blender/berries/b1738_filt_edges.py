# filt_edges
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 1336
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def filt_edges(tag, count, weighted):
    """Event-driven PWM for `count` voices: high duration x:(r2)+, low y:(r4)+, next-edge
    time y:(r0)+ (1/4096 sample from the block start, one's-complemented while high).
    Rises add the voice weight into the X difference buffer, falls subtract it. x0 holds
    the block length. Unweighted: weight 1, y0 = buffer address. Weighted: weights y:(r3)+
    into y0, buffer at r5 (indexed through n5)."""
    def emit(step, op):
        if weighted:
            return f'''    asr #12,a,b
    move b1,n5
    add {step},a
    move x:(r5+n5),b
    {op} y0,b
    move b,x:(r5+n5)
'''
        return f'''    asr #12,a,b
    add y0,b
    move b1,r5
    add {step},a
    move x:(r5),b
    {op} #1,b
    move b,x:(r5)
'''
    return f'''    do #{count},{tag}_edges_end
    move x:(r2)+,x1  y:(r4)+,y1
'''+('    move y:(r3)+,y0\n' if weighted else '')+f'''    move y:(r0),a
    tst a
    jge {tag}_rise
    not a
    move a1,a
{tag}_fall:
    cmp x0,a
    jge {tag}_exit_fall
'''+emit('y1','sub')+f'''{tag}_rise:
    cmp x0,a
    jge {tag}_exit_rise
'''+emit('x1','add')+f'''    jmp {tag}_fall
{tag}_exit_fall:
    sub x0,a
    not a
    jmp {tag}_store
{tag}_exit_rise:
    sub x0,a
{tag}_store:
    move a1,y:(r0)+
    nop
{tag}_edges_end:
'''
