# normalise_isbn
#
# Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
#   file modern_library/main.py, line 166
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

_ISBN_SEPARATORS = re.compile(r"[\s-]+")


def normalise_isbn(raw: str) -> str:
    """Remove hyphens and whitespace, which the server ignores in ISBNs.

    Surrounding whitespace is trimmed by the same rule, since it is
    whitespace too.
    """
    return _ISBN_SEPARATORS.sub("", raw)
