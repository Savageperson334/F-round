# gen_manual_section_head
#
# Copied verbatim from https://github.com/thatfloflo/typst-tyipa
#   file util/make-diacritics.py, line 81
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def gen_manual_section_head(group: str) -> str:
    """Generate a Typst markup heading for a section in the manual."""
    return f"\n== {group.title()}\n\n"
