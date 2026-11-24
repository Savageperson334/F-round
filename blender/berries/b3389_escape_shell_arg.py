# escape_shell_arg
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/gmtpy.py, line 202
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def escape_shell_arg(s):
    '''
    This function should be used for debugging output only - it could be
    insecure.
    '''

    if re.search(r'[^a-zA-Z0-9._/=-]', s):
        return "'" + s.replace("'", "'\\''") + "'"
    else:
        return s
