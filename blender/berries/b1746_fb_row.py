# fb_row
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 2043
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fb_row(control, table, stride_shift):
    # r0 -> table + knob<<stride_shift.
    return f'''    move y:(r6+${control:x}),a
    asr #16,a,a
    move a1,a
    asl #{stride_shift},a,a
    add #>{table},a
    move a1,r0
'''
