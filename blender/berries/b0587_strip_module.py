# strip_module
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file tools/build_standalone.py, line 24
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def strip_module(text, name):
    """Remove the module docstring and turn every intra-package import into `pass` (the names are all in one namespace now)."""
    if name != 'core':
        text = re.sub(r'\A(?:#[^\n]*\n)+', '', text)                    # the credit block (the file starts with the core's once)
        text = re.sub(r'^"""[\s\S]*?"""\n', '', text, count=1)
    text = re.sub(r'^([ \t]*)from \.\w+ import (?:\([^)]*\)|[^\n]*)\n', r'\1pass\n', text, flags=re.M)
    return text
