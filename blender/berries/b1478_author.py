# author
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/web/__init__.py, line 2246
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def author(name):
    """ Returns a Twitter query-by-author-name that can be passed to Twitter.search().
        For example: Twitter().search(author("tom_de_smedt"))
    """
    return "from:%s" % name
