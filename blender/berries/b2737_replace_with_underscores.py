# replace_with_underscores
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/src/utils/utility_functions.py, line 112
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def replace_with_underscores(string):
    '''Replace spaces, slashes and percent signs with underscores or ASCII equivalents.

    Used for sanitising file and folder names produced from user inputs.

    Args:
        string (str): Raw string, e.g. a filter name like ``"488 nm / 50%"``.

    Returns:
        str: Sanitised string safe for use in file paths.
    '''
    s = string.replace(' ', '_').replace('/', '_').replace('%', 'pct')
    return s
