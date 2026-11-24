# conv_K2F
#
# Copied verbatim from https://github.com/KMFleischer/PyEarthScience
#   file Tutorial/lib/dkrz_utils.py, line 117
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def conv_K2F(value):
    """Converts Kelvin to degree Fahrenheit.
       Input parameter:   scalar or array
    """
    if(isinstance(value,(float,int))):
       assert(value >= 0),"value < 0 -> Colder than absolute zero!"
    else:
       assert(value.any() >= 0),"value < 0 -> Colder than absolute zero!"

    value_f = (value-273.15)*(9/5)+32

    if(hasattr(value_f, 'units')):    
       value_f.attrs.update(units='degF')

    return(value_f)
