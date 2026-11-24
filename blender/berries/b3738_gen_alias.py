# gen_alias
#
# Copied verbatim from https://github.com/thatfloflo/typst-tyipa
#   file util/make-diacritics.py, line 64
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def gen_alias(orig: str, alias: str) -> str:
    """Generate code for aliasing a function in Typst."""
    o = []
    o.append('/// Alias for `{orig}`.')
    o.append('#let {alias} = {orig}')
    o.append('\n')
    return "\n".join(o).format(
        orig=orig,
        alias=alias
    )
