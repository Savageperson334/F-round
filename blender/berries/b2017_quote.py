# quote
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_fill.py, line 56
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def quote(text: str, callout: str) -> str:
    """Text as an Obsidian callout: `> [!kind] title` and every line quoted."""
    body = "\n".join(f"> {line}" if line.strip() else ">" for line in text.strip("\n").split("\n"))
    return f"> {callout}\n{body}"
