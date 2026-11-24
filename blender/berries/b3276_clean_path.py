# clean_path
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/client/wadl.py, line 28
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

re_multisl = re.compile(r'/+')

re_rmsite = re.compile(r'https?://[^/]+')


def clean_path(p):
    p = re_rmsite.sub('', p)
    p = re_multisl.sub('/', p)
    if not p.startswith('/'):
        p = '/' + p

    return p
