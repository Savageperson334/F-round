# family_of
#
# Copied verbatim from https://github.com/ductone/orrery
#   file research/modelbench/fetch.py, line 818
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

CLAUDE_FAMS = "opus|sonnet|haiku|fable|mythos"


def family_of(mid):
    m = re.match(r"^claude-(%s)" % CLAUDE_FAMS, mid)
    if m:
        return "claude-" + m.group(1)
    m = re.match(r"^gpt-[\d.]+-(sol|terra|luna|astra)", mid)
    if m:
        return "gpt-" + m.group(1)
    m = re.match(r"^([a-z]+(?:-[a-z]+)?)", re.sub(r"[\d.]+.*$", "", mid) or mid)
    return (m.group(1).rstrip("-") if m else mid) or mid
