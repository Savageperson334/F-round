# remove_version
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/gloo/parser.py, line 31
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def remove_version(code):
    """ Remove any version directive """

    pattern = '\#\s*version[^\r\n]*\n'
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    return regex.sub('\n', code)
