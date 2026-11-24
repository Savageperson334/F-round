# slug
#
# Copied verbatim from https://github.com/FartyPants/fm1-nachtfahrt
#   file tools/manual_html.py, line 110
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def slug(title):
    m = re.match(r"(\d+)\.", title)
    return f"s{m.group(1)}" if m else re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
