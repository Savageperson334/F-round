# what
#
# Copied verbatim from https://github.com/FartyPants/fm1-nachtfahrt
#   file tools/gen_manual_figures.py, line 42
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def what(x, y, t):
    """what a control does, under it (one or two lines, split at |)"""
    a, _, b = t.partition("|")
    return (f'<text x="{x}" y="{y}" text-anchor="middle" class="what">{a}</text>' +
            (f'<text x="{x}" y="{y + 15}" text-anchor="middle" class="what">{b}</text>' if b else ""))
