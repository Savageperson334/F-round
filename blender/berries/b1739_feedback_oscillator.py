# feedback_oscillator
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 1711
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

Q = 1 << 23


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


def q(value):
    return max(-Q, min(Q-1, round(value*Q)))


def sine_a():
    """A1 phase -> interpolated sine in A; B/r0/r4 are preserved."""
    # The shared sine (filt_sine1k): 1,024 points, phase>>14.
    return '''    asr #14,a,a
    and #>$3ff,a
    add #>filt_sine1k,a
    move a1,r5
    nop
    move y:(r5),a
'''


def feedback_oscillator(tag, index, input_code, shape, depth_code='', delayed=False, linear=False):
    phase=f'y:(r6+${32+index:x})'; step=f'x:(r6+${index:x})'
    result=''
    if linear:
        # Linear-FM sine emits the old phase, then advances it, unlike exponential FM.
        result+=input_code+f'''    move a,x0
    move {step},y0
    mpy x0,y0,a
    add y0,a
    move a1,x0
    move {phase},a
    add x0,a  a1,x1
    move a1,{phase}
    move x1,a
'''
    elif input_code:
        if delayed:
            result+=f'''    move y:(r6+$15),a
    tst a
    jeq {tag}_unconnected
'''
        result+=depth_code+input_code+fm_scale(tag,double_depth=True)+f'''    move {step},x0
    move y:(r6+$13),y0
    move y:(r6+$12),x1
    mpy x0,y0,a
    ; Bound before shifting: deep FM must not overflow the accumulator.
    move #>$7ffe00,b
    asr x1,b,b
    cmp b,a
    jgt {tag}_clamp
    asl x1,a,a
    jmp {tag}_step
{tag}_clamp:
    move #>$7ffe00,a
{tag}_step:
    move {phase},x0
    add x0,a
    move a1,{phase}
    move a1,a
'''
        if delayed:
            result+=f'''    jmp {tag}_wave
{tag}_unconnected:
    move {phase},a
    move {step},x0
    add x0,a  a1,x1
    move a1,{phase}
    move x1,a
{tag}_wave:
'''
    else:
        result+=f'''    move {phase},a
    move {step},x0
    add x0,a  a1,x1
    move a1,{phase}
    move x1,a
'''
    if shape=='sine': result+=sine_a()
    elif shape=='saw_offset':
        result+=f'''    move a1,x0
    move #>${q(.8):x},y0
    mpy x0,y0,a
    add #>$7fffff,a
'''
    elif shape in ('pulse','atari_pulse'):
        result+='''    asr a
    and #>$7fffff,a
    move a1,a
'''
        if shape=='pulse': result+='    move y:(r6+$17),b\n'
        else:
            result+='''    move x:(r6+$10),b
    asr b
    add #>$400000,b
'''
        amp=q(.8) if shape=='pulse' else Q-1
        result+=f'''    cmp b,a
    move #>${(-amp)&0xffffff:x},a
    move #>${amp:x},y0
    tlt y0,a
'''
    else:
        amp=Q-1 if shape=='square_offset' else q(.8)
        result+=f'''    tst a
    move #>${amp:x},a
    jge {tag}_square_positive
    neg a
{tag}_square_positive:
'''
        if shape=='square_offset': result+='    add #>$7fffff,a\n'
    return result+f'    move a,x:(r6+${16+index:x})\n'
