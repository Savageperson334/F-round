# vpdb_to_vsmow
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file stratigraphy/isotope_analysis.py, line 210
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

VP_VPDB_TO_VSMOW_INTERCEPT = 30.91

VP_VPDB_TO_VSMOW_SLOPE = 1.03091


def vpdb_to_vsmow(delta_vpdb: float | np.ndarray) -> float | np.ndarray:
    """Convert δ¹⁸O from VPDB to VSMOW using the linear Coplen (1988)
    formula:

        δ_VSMOW = 1.03091 × δ_VPDB + 30.91

    This is the appropriate conversion for *measured* carbonate (CO2
    equilibrated at 25 °C) when the working standard is tied to VPDB
    but the user wants the VSMOW value to feed e.g. Kim & O'Neil (1997).

    Reference: Coplen (1988), ratified by IUPAC.
    """
    return VP_VPDB_TO_VSMOW_SLOPE * np.asarray(delta_vpdb, dtype=float) + VP_VPDB_TO_VSMOW_INTERCEPT
