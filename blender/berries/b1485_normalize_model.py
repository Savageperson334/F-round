# normalize_model
#
# Copied verbatim from https://github.com/cognitivegears/ha-escpos-thermal-printer
#   file custom_components/escpos_printer/capabilities/aliases.py, line 44
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Thermal printers and obsolete output
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

_NORMALIZE_RE = re.compile(r"[^a-z0-9]+")


def normalize_model(name: str) -> str:
    """Lowercase and strip everything but letters/digits ("CT-S601 II" -> "cts601ii")."""
    return _NORMALIZE_RE.sub("", name.casefold())
