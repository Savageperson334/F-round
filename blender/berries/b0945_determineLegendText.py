# determineLegendText
#
# Copied verbatim from https://github.com/ahotovec/REDPy
#   file redpy/plotting.py, line 683
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def determineLegendText(binsize):

    """
    Helper function to determine legend wording

    binsize: Width (in days) of each time bin

    """

    if binsize == 1/24:
        legtext = 'Hour'
    elif binsize == 1:
        legtext = 'Day'
    elif binsize == 7:
        legtext = 'Week'
    elif binsize < 2:
        legtext = '{} Hours'.format(binsize*24)
    else:
        legtext = '{} Days'.format(binsize)

    return legtext
