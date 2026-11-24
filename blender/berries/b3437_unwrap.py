# unwrap
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/squirrel/tool/common.py, line 27
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def unwrap(s):
    if s is None:
        return None
    s = s.strip()
    parts = re.split(r'\n{2,}', s)
    lines = []
    for part in parts:
        plines = part.splitlines()
        if not any(line.startswith('  ') for line in plines):
            lines.append(' '.join(plines))
        else:
            lines.extend(plines)

        lines.append('')

    return '\n'.join(lines)
