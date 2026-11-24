# wrap
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file install.py, line 38
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
        if part.startswith('usage:'):
            lines.extend(part.splitlines())
        else:
            for line in part.splitlines():
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
