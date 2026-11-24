# SearchBoxSize
#
# Copied verbatim from https://github.com/brodeau/gonzag
#   file gonzag/utils.py, line 97
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def SearchBoxSize( res_mod, width_box ):
    '''
    # Returns half of the width, in number of grid points, of the small zoom-box 
    # of the source (model) domain in which NearestPoint() will initially attempt
    # to locate  the nearest point, before falling back on the whole source (model)
    # domain if unsuccessful.                           
    #  => the smaller the faster the search...
    #
    # * res_mod:   horizontal resolution of the model data, in km
    # * width_box: width of the zoom-box in km
    #
    # TODO: shoud take into account the speed of the satellite
    '''
    return int(0.5*width_box/res_mod)
