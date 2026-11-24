# DecodeString
#
# Copied verbatim from https://github.com/ogliore/Tescan-Image-Surface-Acquisition
#   file Python/remote/sem_v2_lib.py, line 14
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def DecodeString(s_in):
    i = 0
    for i in range(0, len(s_in)):
        if s_in[i] == "\x00":
            break            
    return s_in[0:i]
