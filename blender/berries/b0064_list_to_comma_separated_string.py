# list_to_comma_separated_string
#
# Copied verbatim from https://github.com/AstronomyLiveYt/SatTraker
#   file pwi4_client.py, line 698
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def list_to_comma_separated_string(value_list):
    """
    Convert list of values (e.g. [3, 1, 5]) into a comma-separated string (e.g. "3,1,5")
    """

    return ",".join([str(x) for x in value_list])
