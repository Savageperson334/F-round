# grain_wave
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 3250
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def grain_wave(mode):
    """Sign-extended phase in B -> oscillator sample in B: square +32767/-32768, or saw for III."""
    if mode==2:
        return '    asr #8,b,b\n'
    return '    asr #23,b,b\n    eor #>$7fff,b\n'
