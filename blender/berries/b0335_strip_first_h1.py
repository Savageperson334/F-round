# strip_first_h1
#
# Copied verbatim from https://github.com/ItIsMixian/Orrery
#   file scripts/docsite/build_docsite.py, line 110
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

H1_RE = re.compile(r"^#\s+")


def strip_first_h1(text: str) -> str:
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if H1_RE.match(ln):
            del lines[i]
            break
    return "\n".join(lines)
