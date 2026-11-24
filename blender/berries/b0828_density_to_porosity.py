# density_to_porosity
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/petrophysics/petrophysics.py, line 86
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def density_to_porosity(rho, rho_matrix, rho_fluid):
    """
    Get density from a porosity log. Typical values:

        - rho_matrix (sandstone) : 2650 kg/m^3
        - rho_matrix (limestome): 2710 kg/m^3
        - rho_matrix (dolomite): 2876 kg/m^3
        - rho_matrix (anyhydrite): 2977 kg/m^3
        - rho_matrix (salt): 20320 kg/m^3

        - rho_fluid (fresh water): 1000 kg/m^3
        - rho_fluid (salt water): 1100 kg/m^3

    See wiki.aapg.org/Density-neutron_log_porosity.

    Args:
        rho (ndarray): The bulk density log or RHOB.
        rho_matrix (float)
        rho_fluid (float)

    Returns:
        Estimate of porosity as a volume fraction.
    """
    return (rho_matrix - rho) / (rho_matrix - rho_fluid)
