# conv_F2K_2
#
# Copied verbatim from https://github.com/KMFleischer/PyEarthScience
#   file Tutorial/lib/dkrz_utils.py, line 72
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


def conv_F2C(value):
    """Converts degree Fahrenheit to degree Celsius.
       Input parameter:   scalar or array
    """
    value_c = (value-32)*(5/9)

    if(hasattr(value_c, 'units')):    
       value_c.attrs.update(units='degC')

    return(value_c)


def conv_F2K_2(value):
    """Converts degree Fahrenheit to Kelvin.
       Input parameter:   scalar or array
    """
    value_c = conv_F2C(value)

    return(conv_C2K(value_c))
