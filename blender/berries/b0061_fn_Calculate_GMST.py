# fn_Calculate_GMST
#
# Copied verbatim from https://github.com/AshivDhondea/Satellite_Ground_Track_Plotting_Python
#   file AstroFunctions.py, line 66
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fn_Calculate_GMST(JD):
    """
    Calculates the Greenwich Mean Sidereal Time according to eqn 3-47 on page 188 in Vallado.
    Date: 05 October 2016
    Edit: 06 October 2016: CAUTION: theta_GMST is output in [degrees] rather than in [radians], 
    unlike most of the angles in this file.
    """
    T_UT1 = (JD - 2451545.0)/36525.0
    theta_GMST = 67310.54841 + (876600.0*60*60 + 8640184.812866)*T_UT1 + 0.093104 * T_UT1**2 - 6.2e-6 * T_UT1**3;

    while theta_GMST > 86400.0:
        theta_GMST = theta_GMST - 86400;

    theta_GMST = theta_GMST/240.0;
    theta_GMST = theta_GMST - 360; # in [deg] not [rad] !!!!!!!!!!!!!!!!!!!!!!!!!!!
    return theta_GMST
