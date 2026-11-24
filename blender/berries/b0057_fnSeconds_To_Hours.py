# fnSeconds_To_Hours
#
# Copied verbatim from https://github.com/AshivDhondea/Satellite_Ground_Track_Plotting_Python
#   file AstroFunctions.py, line 19
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fnSeconds_To_Hours(time_period):
    """
    Convert from seconds to hours, minutes and seconds.

    Date: 16 October 2016
    """
    num_hrs = int(time_period/(60.*60.));
    time_period =time_period - num_hrs*60.*60.;
    num_mins = int(time_period/60.);
    num_secs = time_period - num_mins*60.;
    return num_hrs,num_mins,num_secs
