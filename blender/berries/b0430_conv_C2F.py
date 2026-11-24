# conv_C2F
#
# Copied verbatim from https://github.com/KMFleischer/PyEarthScience
#   file Tutorial/lib/dkrz_utils.py, line 136
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def conv_C2F(value):
    """Converts degree Celsius to degree Fahrenheit.
       Input parameter:   scalar or array
    """
    value_f = (value*(9/5))+32

    if(hasattr(value_f, 'units')):    
       value_f.attrs.update(units='degF')

    return(value_f)
