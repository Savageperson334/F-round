# decamel
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/__init__.py, line 329
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def decamel(s, separator="_"):
    """ Returns the string with CamelCase converted to underscores, e.g.,
        decamel("TomDeSmedt", "-") => "tom-de-smedt"
        decamel("getHTTPResponse2) => "get_http_response2"
    """
    s = re.sub(r"([a-z0-9])([A-Z])", "\\1%s\\2" % separator, s)
    s = re.sub(r"([A-Z])([A-Z][a-z])", "\\1%s\\2" % separator, s)
    s = s.lower()
    return s
