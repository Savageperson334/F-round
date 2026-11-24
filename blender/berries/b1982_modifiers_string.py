# modifiers_string
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/app/window/key.py, line 91
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

MOD_ALT         = 1 << 2

MOD_CAPSLOCK    = 1 << 3

MOD_COMMAND     = 1 << 6

MOD_CTRL        = 1 << 1

MOD_NUMLOCK     = 1 << 4

MOD_OPTION      = 1 << 7

MOD_SCROLLLOCK  = 1 << 8

MOD_SHIFT       = 1 << 0


def modifiers_string(modifiers):
    '''Return a string describing a set of modifiers.

    Example::

        >>> modifiers_string(MOD_SHIFT | MOD_CTRL)
        'MOD_SHIFT|MOD_CTRL'

    :Parameters:
        `modifiers` : int
            Bitwise combination of modifier constants.

    :rtype: str
    '''
    mod_names = []
    if modifiers & MOD_SHIFT:
        mod_names.append('MOD_SHIFT')
    if modifiers & MOD_CTRL:
        mod_names.append('MOD_CTRL')
    if modifiers & MOD_ALT:
        mod_names.append('MOD_ALT')
    if modifiers & MOD_CAPSLOCK:
        mod_names.append('MOD_CAPSLOCK')
    if modifiers & MOD_NUMLOCK:
        mod_names.append('MOD_NUMLOCK')
    if modifiers & MOD_SCROLLLOCK:
        mod_names.append('MOD_SCROLLLOCK')
    if modifiers & MOD_COMMAND:
        mod_names.append('MOD_COMMAND')
    if modifiers & MOD_OPTION:
        mod_names.append('MOD_OPTION')
    return '|'.join(mod_names)
