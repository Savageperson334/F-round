# resolve
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file packs/pitch.py, line 26
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def resolve(p, zone=None):
    out = {k: v for k, v in p.items() if k != 'by_mode'}
    for row in p.get('by_mode', []) if zone is not None else []:
        if row['zone'] == zone:
            out.update({k: v for k, v in row.items() if k != 'zone'})
    return out
