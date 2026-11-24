# substitute
#
# Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
#   file archaeology/scenarios.py, line 176
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

_PLACEHOLDER = re.compile(r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}")


def substitute(text: str, variables: dict[str, str]) -> str:
    """Replace ``{{name}}`` with its bound value; unbound placeholders stay as written."""
    return _PLACEHOLDER.sub(lambda m: variables.get(m.group(1), m.group(0)), text)
