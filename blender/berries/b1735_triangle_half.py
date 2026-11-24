# triangle_half
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 798
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def triangle_half(tag):
    """A1 phase -> half-amplitude triangle in A; avoids clipping its positive peak."""
    return f'''    move a1,x0
    abs a
    sub #>$400000,a
    abs a
    move #>$400000,b
    sub a,b
    move x0,a
    tst a
    jge {tag}_triangle_positive
    neg b
{tag}_triangle_positive:
    move b,a
'''
