# strip_whitespace
#
# Copied verbatim from https://github.com/jesserobertson/earthchem-pyclient
#   file earthchem/documentation.py, line 16
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def strip_whitespace(string):
    """ Strip newline, tab and multple whitespace from a string
    """
    return re.sub(' +', ' ',
                  string.replace('\n', ' ').replace('\t', ' ').strip())
