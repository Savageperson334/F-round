# choice
#
# Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
#   file pipeline/quests.py, line 37
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def choice(at, ask, options, reveal, checks=()):
    """options: the right answer first; the page shuffles them."""
    return dict(kind="choice", at=at, ask=ask, options=options, reveal=reveal, checks=list(checks))
