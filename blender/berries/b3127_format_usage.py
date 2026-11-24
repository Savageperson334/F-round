# format_usage
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file maintenance/argparse_help_to_rst.py, line 118
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def indent(n, lines):
    return [' ' * n + line if line else '' for line in lines]


def format_usage(program, s):
    return ['.. application:: %s' % program, ''] \
        + indent(0, ['.. code-block:: none', ''] + indent(4, s.splitlines()))
