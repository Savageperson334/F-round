# fm_scale
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 768
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fm_scale(tag, double_depth=False):
    # Match the original 16-bit modulation input and default eight-octave depth.
    # The table preserves the original de Soras quadratic, not an ideal exp2.
    return '''    move a,x0
    move y:(r6+$11),y0
    mpy x0,y0,a
'''+('    asl a\n' if double_depth else '')+'''    asr #8,a,a
    move a1,x0
    asr #12,a,a
    add #>1,a
    move a1,y:(r6+$12)
    move x0,a
    and #>$fff,a
    add #>fm_mantissa,a
    move a1,r5
    nop
    move y:(r5),a
    move y:(r6+$12),b
    tst b
'''+f'''    jge {tag}_positive
    neg b
    move b,x1
    asr x1,a,a
    clr b
    move b,y:(r6+$12)
{tag}_positive:
    move a1,y:(r6+$13)
'''
