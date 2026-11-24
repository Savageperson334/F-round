# wrap
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/squirrel/tool/common.py, line 45
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re
import textwrap


def wrap(s):
    lines = []
    parts = re.split(r'\n{2,}', s)
    for part in parts:
        plines = part.splitlines()
        if part.startswith('usage:') \
                or all(line.startswith('    ') for line in plines):
            lines.extend(plines)
        else:
            for line in plines:
                if not line:
                    lines.append(line)
                if not line.startswith(' '):
                    lines.extend(
                        textwrap.wrap(line, 79,))
                else:
                    lines.extend(
                        textwrap.wrap(line, 79, subsequent_indent=' '*24))

        lines.append('')

    return '\n'.join(lines)
