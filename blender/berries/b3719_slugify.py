# slugify
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file presets/manager.py, line 36
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def slugify(name: str) -> str:
    """Filesystem-safe slug; empty results fall back to ``preset``."""
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", name.strip()).strip("._-")
    return slug or "preset"
