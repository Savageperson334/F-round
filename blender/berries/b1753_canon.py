# canon
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file packs/assembly.py, line 47
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

CANON={('x0','x0'),('y0','y0'),('x1','x0'),('y1','y0'),('x0','y1'),('y0','x0'),('x1','y0'),('y1','x1')}


def canon(ins):
    m=re.match(r'^(mpy|mac|mpyr|macr)\s+(-?)(x0|x1|y0|y1),(x0|x1|y0|y1),(a|b)(.*)$',ins,re.I)
    if m:
        op,neg,s1,s2,d,rest=m.groups()
        if (s1,s2) not in CANON and (s2,s1) in CANON: s1,s2=s2,s1
        ins=f'{op} {neg}{s1},{s2},{d}{rest}'
    return ins
