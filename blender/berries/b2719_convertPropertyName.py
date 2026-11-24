# convertPropertyName
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/scripts/HamamatsuTest/hamamatsu_camera.py, line 200
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def convertPropertyName(p_name):
    """
    "Regularizes" a property name. We are using all lowercase names with
    the spaces replaced by underscores.
    """
    return p_name.lower().replace(" ", "_")
