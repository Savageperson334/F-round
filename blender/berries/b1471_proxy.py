# proxy
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/web/__init__.py, line 310
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def proxy(host, protocol="https"):
    """ Returns the value for the URL.open() proxy parameter.
        - host: host address of the proxy server.
    """
    return (host, protocol)
