# format_data_size
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/src/utils/utility_functions.py, line 64
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_data_size(bytes):
    '''
    Converts bytes into human-readable format (kb, MB, GB)
    '''
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except Exception as e:
        print(f"{e}")
        return None
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.1f GB" % (G)
        else:
            return "%.1f MB" % (M)
    else:
        return "%.1f kb" % (kb)
