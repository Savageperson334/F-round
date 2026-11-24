# is_boolean
#
# Copied verbatim from https://github.com/boschresearch/pcg_gazebo
#   file pcg_gazebo/utils.py, line 413
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def is_boolean(obj):
    """Test if input object is a boolean.

    > *Input arguments*

    * `obj`: Input variable.

    > *Returns*

    `True`, if `obj` is a boolean.
    """
    return isinstance(obj, bool) or obj in [0, 1]
