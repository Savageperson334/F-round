# get_bu_sec_conv_factor
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 410
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_bu_sec_conv_factor(vol, ihm):
    """Computes the factor that converts seconds into burnup units (MWd/kg) from a given volume and a Initial Heavy Metal mass (IHM).

    Parameters
    ----------
    vol: float
        Volume of the region
    ihm: float
        Initial Heavy Metal mass of the region
    """
    bu_sec_conv_factor = vol*1e-3/(ihm*24*3600) # Unit in L/g

    return bu_sec_conv_factor
