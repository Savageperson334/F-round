# slug
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_fill.py, line 66
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def slug(heading: str) -> str:
    """
    A heading's id as GitHub makes it, and the notebook's tab with it (markdown.js):
    the text a reader sees, in lower case, every character but a letter, a digit,
    `_`, `-` or a space dropped, each space a dash.
    """
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", heading)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]*>|[*`$]|(?<!\w)_|_(?!\w)", "", text)
    return re.sub(r"[^\w\- ]", "", text.strip().lower()).replace(" ", "-") or "section"
