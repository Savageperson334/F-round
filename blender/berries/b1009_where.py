# where
#
# Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
#   file pipeline/quests.py, line 42
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def T(en, nl):
    return dict(en=en, nl=nl)


def where(at, name, reveal, checks):
    """A photo and a name; the player taps the map where they think it stands and scores by distance."""
    return dict(kind="where", at=at, riddle=T(f"Where is {name[0]}?", f"Waar staat {name[1]}?"), reveal=reveal,
                checks=list(checks), clue="today")
