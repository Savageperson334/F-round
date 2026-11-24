# describe_address
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/server.py, line 69
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def describe_address(address):
    substitutions = {
        '': 'all available interfaces',
        '::': 'all available IPv6 interfaces',
        '0.0.0.0': 'all available IPv4 interfaces'}

    return substitutions.get(address, 'address "%s"' % address)
