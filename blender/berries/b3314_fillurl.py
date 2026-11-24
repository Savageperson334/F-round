# fillurl
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gf/ws.py, line 88
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

g_site_abbr = {
    'localhost': 'http://localhost:8080',
    'kinherd': 'https://gf.pyrocko.org',
    'pyrocko': 'https://gf.pyrocko.org',
}


def fillurl(url, site, service, majorversion, method='query'):
    return url % dict(
        site=g_site_abbr.get(site, site),
        service=service,
        majorversion=majorversion,
        method=method)
