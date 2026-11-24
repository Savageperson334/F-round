# url_address
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/server.py, line 78
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def url_address(address):
    if '' == address or '::' == address:
        return '[::1]'
    elif '0.0.0.0' == address:
        return '127.0.0.1'
    elif ':' in address:
        return '[%s]' % address
    else:
        return address
