# fb_step_table
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 2069
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fb_fm_var():
    # a = min(x1, (x0*y0)<<y1), clamped before the shift (exponents reach 12).
    return '''    mpy x0,y0,a
    move x1,b
    asr y1,b,b
    cmp b,a
    tgt b,a
    asl y1,a,a
'''


def fb_plain(base='n1'):
    # Flags gt: the node is delayed and the ring is not yet valid, so it runs
    # unmodulated (base s, delta 0) on phase-s (offset s) to emit its old phase.
    # In: a = other-base, base = base step, x0 = s.
    return f'''    clr a ifgt
    move a,x:(r2)
    move {base},a
    tfr x0,a ifgt
    move a,y:(r2)+
    tfr x0,a
    clr a ifle
    move a,x:(r4)+
'''


def fb_step_table(count, tag):
    # For each node: s=min(cap,rate*pitch), the two FM steps from y:(r1)+
    # (mantissa, shift) pairs and a delayed flag: y:(r2) <- base,
    # x:(r2)+ <- other-base, x:(r4)+ <- phase offset (see fb_plain).
    # Expects r0 rates, r1 FM constants, r2 L table, r4 offsets, n0 pitch,
    # n5 valid, x1 cap.
    return f'''    do #{count},{tag}_setup_end
    move y:(r0)+,x0
    move n0,y0
    mpy x0,y0,a
    asl #2,a,a
    cmp x1,a
    tgt x1,a
    move a,x0
    move y:(r1)+,y0
    move y:(r1)+,y1
'''+fb_fm_var()+'''    move a,n1
    move y:(r1)+,y0
    move y:(r1)+,y1
'''+fb_fm_var()+'''    move n1,y0
    sub y0,a
    move y:(r1)+,b
    move n5,y0
    sub y0,b
'''+fb_plain()+f'''{tag}_setup_end:
'''
