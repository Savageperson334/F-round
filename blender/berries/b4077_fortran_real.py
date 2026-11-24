# fortran_real
#
# Copied verbatim from https://github.com/ymatterlab/ycrystal
#   file src/ycrystal/io/readers.py, line 579
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

_FORTRAN_REAL = re.compile(r"^[+-]?(?:\d+\.?\d*|\.\d+)[dD][+-]?\d+$")


def fortran_real(token: str) -> str:
    """Return a Fortran real with a ``D`` exponent in the ``E`` notation Python reads.

    pw.x reads masses and cell vectors with Fortran, which accepts ``16.D0`` or
    ``1.5d-3``; other text is returned unchanged.

    Examples
    --------
    >>> from ycrystal.io.readers import fortran_real
    >>> fortran_real("16.D0"), fortran_real("-1.5d-3"), fortran_real("Si.pbe-d.UPF")
    ('16.E0', '-1.5e-3', 'Si.pbe-d.UPF')
    """
    if _FORTRAN_REAL.match(token):
        return token.replace("D", "E").replace("d", "e")
    return token
