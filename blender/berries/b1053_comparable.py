# comparable
#
# Copied verbatim from https://github.com/amacias/octo-vave
#   file tools/fm1_site.py, line 81
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import json


def comparable(snap):
    """The snapshot without the fields that change on every run."""
    s = json.loads(json.dumps(snap))
    s.pop("generated_at", None)
    for k in ("checked", "stats"):
        s.get("discovery", {}).pop(k, None)
    s.get("releases", {}).pop("checked", None)
    return s
