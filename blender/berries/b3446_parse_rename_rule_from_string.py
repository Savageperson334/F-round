# parse_rename_rule_from_string
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/squirrel/tool/commands/jackseis.py, line 56
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def parse_rename_rule_from_string(s):
    s = s.strip()
    if re.match(r'^([^:,]*:[^:,]*,?)+', s):
        return dict(
            x.split(':') for x in s.strip(',').split(','))
    else:
        return s
