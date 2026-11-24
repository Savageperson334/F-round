# dispersion_parameter
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/anisotropy.py, line 165
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def dispersion_parameter(qp):
    """
    Kjartansson (1979). Journal of Geophysical Research, 84 (B9),
    4737-4748. DOI: 10.1029/JB084iB09p04737.
    """
    return np.arctan(1/qp) / np.pi
