# strip_end
#
# Copied verbatim from https://github.com/MartinThoma/hwrt
#   file hwrt/datasets/mfrdb.py, line 87
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def strip_end(text, suffix):
    """Strip `suffix` from the end of `text` if `text` has that suffix."""
    if not text.endswith(suffix):
        return text
    return text[: len(text) - len(suffix)]
