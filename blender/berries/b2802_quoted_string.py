# quoted_string
#
# Copied verbatim from https://github.com/morganjwilliams/exploratory-geochemistry
#   file src/text_accessories.py, line 3
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def quoted_string(s):
    #if " " in s or '-' in s or '_' in s:
    s = f'''"{s}"'''
    return s
