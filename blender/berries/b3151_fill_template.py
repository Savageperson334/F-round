# fill_template
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/config.py, line 135
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fill_template(tmpl, config_type):
    tmpl = tmpl .format(
        module=('.' + config_type) if config_type != 'pyrocko' else '')
    return tmpl
