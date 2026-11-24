# format_arg_group
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file maintenance/argparse_help_to_rst.py, line 131
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_arg_group(program, part):
    part = list(part)
    lines = ['**%s**' % part.pop(0), '']
    for arg, description in part:
        lines.extend([
            '.. describe:: %s' % arg, '', '    %s' % description, ''])

    return lines
