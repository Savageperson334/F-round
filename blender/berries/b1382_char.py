# char
#
# Copied verbatim from https://github.com/cldf/multicode
#   file src/multicode/util.py, line 13
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

CODE_POINT_PATTERN = re.compile(r'U\+[0-9a-fA-F]{4}$')


def char(spec):
    if CODE_POINT_PATTERN.match(spec):
        return chr(int(spec.replace('U+', '0x'), base=16))
    return spec
