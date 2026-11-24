# pick
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 877
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

LANG = "it"

LANGUAGES = ("it", "en")


def pick(pair):
    """The current language's half of an (it, en) pair."""
    return pair[LANGUAGES.index(LANG)]
