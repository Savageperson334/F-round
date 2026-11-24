# symbol_string
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/app/window/key.py, line 124
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_key_names = {}


def symbol_string(symbol):
    '''Return a string describing a key symbol.

    Example::

        >>> symbol_string(BACKSPACE)
        'BACKSPACE'

    :Parameters:
        `symbol` : int
            Symbolic key constant.

    :rtype: str
    '''
    if symbol < 1 << 32:
        return _key_names.get(symbol, str(symbol))
    else:
        return 'user_key(%x)' % (symbol >> 32)
