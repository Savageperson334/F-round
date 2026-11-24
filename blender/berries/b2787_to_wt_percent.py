# to_wt_percent
#
# Copied verbatim from https://github.com/morganjwilliams/202103-MQ-pyrolite-workshop
#   notebook notebooks/01_jupyter_python.ipynb (its code cells joined in order; line 105 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_wt_percent(x, # this is an argument
                  from_units='ppm' # this is a keyword argument
                 ):
    """ 
    Convert a value to wt%.

    Parameters
    ----------
    x : float | array
        Value to convert units for.
    from_units : str
        Current units the value is in.

    Returns
    -------
    float
    """
    if from_units == 'wt%':
        pass
    elif from_units == 'ppm':
        x /= 10000
    else:
        raise NotImplementedError
    return x
