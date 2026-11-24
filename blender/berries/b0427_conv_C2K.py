# conv_C2K
#
# Copied verbatim from https://github.com/KMFleischer/PyEarthScience
#   file Tutorial/lib/dkrz_utils.py, line 83
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def conv_C2K(value):
    """Converts degree Celsius to Kelvin.
       Input parameter:   scalar or array
    """
    value_k = value+273.15

    if(hasattr(value_k, 'units')):    
       value_k.attrs.update(units='K')

    return(value_k)
