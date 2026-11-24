# safe_version
#
# Copied verbatim from https://github.com/amacias/octo-vave
#   file server.py, line 248
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def safe_version(v):
    v = re.sub(r"[^A-Za-z0-9._\-]", "_", str(v))[:48]
    return v or "unknown"
