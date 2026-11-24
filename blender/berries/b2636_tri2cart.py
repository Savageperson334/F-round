# tri2cart
#
# Copied verbatim from https://github.com/marcoalopez/ternary_plots
#   file mpl_ternary.py, line 38
#   licence (as GitHub reports it): MPL-2.0   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def tri2cartX(upper_apex, right_apex, left_apex):
    """ Converts ternary to Cartesian x coordinates."""
    return 0.5 * (upper_apex + 2 * right_apex) / (upper_apex + right_apex + left_apex)


def tri2cartY(upper_apex, right_apex, left_apex):
    """ Converts ternary to Cartesian y coordinates."""
    return (3**0.5 / 2) * upper_apex / (upper_apex + right_apex + left_apex)


def tri2cart(upper_apex, right_apex, left_apex):
    """ Converts ternary to Cartesian coordinates.
    Normalises input values and returns Cartesian
    coordinates x, y as a float or array.

    Parameters
    ----------
    upper_apex : numeric or array-like
        coordinate related to the upper corner/apex
    right_apex : numeric or array-like
        coordinate related to the right corner/apex
    left_apex : numeric or array-like
        coordinate related to the left corner/apex

    Example
    -------
    x, y = tri2cart(20, 10.5, 3.2)
    """

    # normalize
    total = upper_apex + right_apex + left_apex
    upper_apex = upper_apex / total
    right_apex = right_apex / total
    left_apex = left_apex / total

    return tri2cartX(upper_apex, right_apex, left_apex), tri2cartY(upper_apex, right_apex, left_apex)
