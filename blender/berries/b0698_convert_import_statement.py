# convert_import_statement
#
# Copied verbatim from https://github.com/ScopeFoundry/ScopeFoundry
#   file tools/features/new_app.py, line 9
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def convert_import_statement(import_line: str) -> str:
    pattern = r"from ScopeFoundry\.examples\.((?:\w+\.)*\w+) imp(\w+)"
    replacement = r"from \1 imp\2"
    new_import = re.sub(pattern, replacement, import_line)
    return new_import
