# autolink
#
# Copied verbatim from https://github.com/paleo-data/paleo-data.github.io
#   file scripts/utils.py, line 16
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def autolink(text: str, fmt: str = "markdown", class_: str = None) -> str:
    """Locates and adds anchor tags to external links in text"""
    for url in set(re.findall(r"https?://[^\s]+", text)):
        strip_chars = ",."
        if "(" not in url:
            strip_chars += ")"
        url = url.rstrip(strip_chars)
        if fmt == "html" and class_:
            text = text.replace(url, f'<a href="{url}" class="{class_}">{url}</a>')
        elif fmt == "html":
            text = text.replace(url, f'<a href="{url}">{url}</a>')
        elif fmt == "markdown":
            text = text.replace(url, f"[{url}]({url})")
    return text
