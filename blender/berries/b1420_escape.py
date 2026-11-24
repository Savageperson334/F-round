# escape
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/search.py, line 1015
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def escape(string):
    """ Returns the string with control characters for Pattern syntax escaped.
        For example: "hello!" => "hello\!".
    """
    for ch in ("{", "}", "[", "]", "(", ")", "_", "|", "!", "*", "+", "^"):
        string = string.replace(ch, "\\" + ch)
    return string
