# clean_default_string
#
# Copied verbatim from https://github.com/kcsapp/pygrowl
#   file src/growl/tools/parse_compas_options.py, line 98
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

STRAY_QUOTE_CHARS_RE = re.compile("[`‘’“”„‚‹›«»]")


def clean_default_string(value: str) -> str:
    """Remove backtick and non-ASCII quotation-mark characters from a raw
    default-value string."""
    return STRAY_QUOTE_CHARS_RE.sub("", value)
