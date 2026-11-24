# ehash
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/model/event.py, line 34
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import base64
import hashlib


def ehash(s):
    return str(base64.urlsafe_b64encode(
        hashlib.sha1(s.encode('utf8')).digest()).decode('ascii'))
