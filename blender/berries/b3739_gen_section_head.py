# gen_section_head
#
# Copied verbatim from https://github.com/thatfloflo/typst-tyipa
#   file util/make-diacritics.py, line 76
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def gen_section_head(group: str) -> str:
    """Generate a comment for section headin in Typst."""
    return f"/*** {group.capitalize()} diacritics***/\n\n"
