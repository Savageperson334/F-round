# get_auger_monthly_model
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/atmosphere/models.py, line 191
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_auger_monthly_model(month):
    """ Helper function to get the correct model number for monthly Auger atmospheres """
    return month + 17
