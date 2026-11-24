# knob_index
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 907
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def knob_index(control, table, scale=0):
    """r0 = table + knob*(2**scale); fractional knob bits stay in a0 and are ignored."""
    return f'''    move y:(r6+${control:x}),a
    asr #16,a,a
'''+(f'    lsl #{scale},a\n' if scale else '')+f'''    add #>{table},a
    move a1,r0
'''
