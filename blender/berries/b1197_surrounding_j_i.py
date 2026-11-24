# surrounding_j_i
#
# Copied verbatim from https://github.com/brodeau/gonzag
#   file gonzag/bilin_mapping.py, line 194
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def surrounding_j_i( jP, iP, Ny, Nx, k_ew_per=-1 ):
    '''
    # Returns: "-1" when the index does not exist!
    '''
    jPm1 = jP-1
    jPp1 = jP+1
    iPm1 = iP-1
    iPp1 = iP+1
    #
    if jPp1 == Ny:
        jPp1 = -1 ; # Flag!
    #
    if iPm1 == -1:
        if k_ew_per>=0: iPm1 = Nx - k_ew_per - 1
    if iPp1 == Nx:
        iPp1 = -1 ; # Flag!
        if k_ew_per>=0: iPp1 =      k_ew_per
    #
    return jPm1, jPp1, iPm1, iPp1
