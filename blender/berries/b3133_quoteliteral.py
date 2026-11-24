# quoteliteral
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file maintenance/drone-matterpost.py, line 7
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def quoteliteral(s):
    s = '\n'.join('  '+x for x in s.splitlines())
    return '''```
%s
```
''' % s
