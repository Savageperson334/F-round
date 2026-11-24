# pretty_array_name
#
# Copied verbatim from https://github.com/dmentipl/plonk
#   file src/plonk/utils/strings.py, line 52
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def _rreplace(s, old, new, occurrence):
    # From https://stackoverflow.com/a/2556252/12951362
    li = s.rsplit(old, occurrence)
    return new.join(li)


def pretty_array_name(s: str) -> str:
    """Prettify an array name string.

    Parameters
    ----------
    s
        The string.

    Returns
    -------
    str
    """
    NUM_DUST_MAX = 100

    for v in ['x', 'y', 'z', 'R', 'r', 'phi', 'theta']:
        if s.endswith(f'_{v}'):
            s = _rreplace(s, f'_{v}', f' ({v})', 1)
    for v in [f'{n:03}' for n in range(NUM_DUST_MAX)]:
        if s.endswith(f'_{v}'):
            s = _rreplace(s, f'_{v}', f' ({v})', 1)
    if s.endswith('_tot'):
        s = _rreplace(s, '_tot', ' (total)', 1)
    if s.endswith('_mag'):
        s = _rreplace(s, '_mag', ' (magnitude)', 1)
    if len(s) > 1:
        s = s.capitalize()
    return s.replace('_', ' ')
