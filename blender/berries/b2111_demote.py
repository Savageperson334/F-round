# demote
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/tools/compose_reference.py, line 83
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def demote(body: str) -> str:
    """Every heading of a section one level down, outside code fences."""
    out, fenced = [], False
    for line in body.split("\n"):
        if line.startswith("```"):
            fenced = not fenced
        if not fenced and re.match(r"^#{2,5} ", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)
