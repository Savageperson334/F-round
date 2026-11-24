# format_text
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file maintenance/argparse_help_to_rst.py, line 123
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_text(program, s):
    lines = s.splitlines()
    if all(line.startswith('    ') for line in lines):
        return ['.. code-block:: none', ''] + lines + ['']
    else:
        return [' '.join(lines), '']
