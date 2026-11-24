# href
#
# Copied verbatim from https://github.com/Reytian/fm1-min1
#   file tools/manual_html.py, line 92
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

REPO = "https://github.com/Reytian/fm1-min1"

SITE = "https://reytian.github.io/fm1-min1/"


def href(url):
    """a README link on the site: the site's own pages relative, files of the repository on GitHub"""
    if url.startswith(SITE):
        return "../" + url[len(SITE):]
    if re.match(r"[a-z][a-z0-9+.-]*:|#", url, re.I):
        return url
    path, _, frag = url.partition("#")
    return f"{REPO}/blob/main/{path}" + (f"#{frag}" if frag else "")
