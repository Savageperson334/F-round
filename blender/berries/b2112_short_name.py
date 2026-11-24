# short_name
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/tools/compose_reference.py, line 100
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def short_name(title: str) -> str:
    """An old page's short name, for a heading it shares with another: its title up to a colon or comma."""
    return re.split(r"[:,?]", re.sub(r"\s*\(.*?\)", "", title))[0].strip().lower()
