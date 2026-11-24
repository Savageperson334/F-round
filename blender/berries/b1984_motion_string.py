# motion_string
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/app/window/key.py, line 143
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_motion_names = {}


def motion_string(motion):
    '''Return a string describing a text motion.

    Example::

        >>> motion_string(MOTION_NEXT_WORD):
        'MOTION_NEXT_WORD'

    :Parameters:
        `motion` : int
            Text motion constant.

    :rtype: str
    '''
    return _motion_names.get(motion, str(motion))
