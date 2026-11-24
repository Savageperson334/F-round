# buttons_string
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/app/window/mouse.py, line 41
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

LEFT    = 1 << 1

MIDDLE  = 1 << 2

NONE    = 1 << 0

RIGHT   = 1 << 3


def buttons_string(buttons):
    '''Return a string describing a set of active mouse buttons.

    Example::

        >>> buttons_string(LEFT | RIGHT)
        'LEFT|RIGHT'

    :Parameters:
        `buttons` : int
            Bitwise combination of mouse button constants.

    :rtype: str
    '''
    button_names = []
    if buttons & NONE:
        button_names.append('NONE')
    if buttons & LEFT:
        button_names.append('LEFT')
    if buttons & MIDDLE:
        button_names.append('MIDDLE')
    if buttons & RIGHT:
        button_names.append('RIGHT')
    return '|'.join(button_names)
