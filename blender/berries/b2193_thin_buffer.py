# thin_buffer
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/backend.py, line 100
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def thin_buffer(buffer, buffer_thinning, ensure_last=True):
    """
    Reduce a list of objects by a given value.

    Parameters
    ----------
    buffer : list
        of objects to be thinned
    buffer_thinning : int
        every nth object in list is returned
    ensure_last : bool
        enable to ensure that last object in list is returned
    """
    if ensure_last:
        write_buffer = buffer[-1::-buffer_thinning]
        write_buffer.reverse()
    else:
        write_buffer = buffer[::buffer_thinning]
    return write_buffer
