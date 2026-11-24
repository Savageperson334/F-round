# outputFileTopHeader
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/strings.py, line 5
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def outputFileTopHeader(programType):
    return f"\
# Dot Scanner (https://github.com/bdavis222/dotscanner)\n\
# Generated output file for {programType.lower()} measurement\n#"
