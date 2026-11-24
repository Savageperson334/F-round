# numbers
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/tools/rewrite_check.py, line 59
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import collections
import re

NUMBER = re.compile(r"(?<![\w.])[−-]?\d+(?:[,.]\d+)*(?:%)?")


def numbers(text: str) -> collections.Counter:
    found = collections.Counter()
    for n in NUMBER.findall(text):
        n = n.replace("−", "-").rstrip("%")
        if n.replace(",", "").replace(".", "").lstrip("-").isdigit():
            found[n.lstrip("-")] += 1
    return found
