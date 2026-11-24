# strip_element
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/web/__init__.py, line 934
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def strip_element(string, tag, attributes=""):
    """ Removes all elements with the given tagname and attributes from the string.
        Open and close tags are kept in balance.
        No HTML parser is used: strip_element(s, "a", 'class="x"') matches
        '<a class="x">' or '<a href="x" class="x">' but not "<a class='x'>".
    """
    s = string.lower() # Case-insensitive.
    t = tag.strip("</>")
    a = (" " + attributes.lower().strip()).rstrip()
    i = 0
    j = 0
    while j >= 0:
        #i = s.find("<%s%s" % (t, a), i)
        m = re.search(r"<%s[^\>]*?%s" % (t, a), s[i:])
        i = i + m.start() if m else -1
        j = s.find("</%s>" % t, i + 1)
        opened, closed = s[i:j].count("<%s" % t), 1
        while opened > closed and j >= 0:
            k = s.find("</%s>" % t, j + 1)
            opened += s[j:k].count("<%s" % t)
            closed += 1
            j = k
        if i < 0:
            return string
        if j < 0:
            return string[:i]
        string = string[:i] + string[j + len(t) + 3:]; s = string.lower()
    return string
