# decomment
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/squirrel/tool/commands/template.py, line 200
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def decomment(s):
    out = []
    for line in s.splitlines():
        line = re.sub(r'#.+', '', line)
        if line.strip():
            out.append(line)

    return '\n'.join(out)
