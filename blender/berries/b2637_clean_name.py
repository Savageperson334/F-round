# clean_name
#
# Copied verbatim from https://github.com/marksweiss/tastywaves
#   file tools/fm1_wavetable.py, line 238
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def clean_name(name):
    s = re.sub(r'[^A-Z0-9 ._-]', '', name.upper())[:8].strip()
    return s or 'USER'
