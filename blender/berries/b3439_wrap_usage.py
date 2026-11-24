# wrap_usage
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/squirrel/tool/common.py, line 69
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import textwrap


def wrap_usage(s):
    lines = []
    for line in s.splitlines():
        if not line.startswith('usage:'):
            lines.append(line)
        else:
            lines.extend(textwrap.wrap(line, 79, subsequent_indent=' '*24))

    return '\n'.join(lines)
