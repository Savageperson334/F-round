# fb_fm_row
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 1928
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fb_fm_row(control, table):
    # r0 -> four words (mantissa+, shift+, mantissa-, shift-) for this knob.
    return f'''    move y:(r6+${control:x}),a
    asr #16,a,a
    move a1,a
    tfr a,b
    addl b,a
    add #>{table},a
    move a1,r0
    nop
'''
