# prep_text
#
# Copied verbatim from https://github.com/nthmost/artery-thermal
#   file participant.py, line 38
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Physical art output, plotters, paper and textile machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def prep_text(text):
    """Replace curly apostrophes with straight ones."""
    return text.replace('\u2018', "'").replace('\u2019', "'")
