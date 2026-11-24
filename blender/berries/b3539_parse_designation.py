# parse_designation
#
# Copied verbatim from https://github.com/rlseaman/neolyzer
#   file scripts/diagnostics/diagnose_missing.py, line 14
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def parse_designation(line):
    """Extract designation from MPC format line"""
    if len(line) >= 7:
        return line[0:7].strip()
    return None
