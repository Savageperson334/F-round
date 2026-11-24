# parse_bauds
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/core.py, line 1140
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def parse_bauds(value):
    """'auto' -> (200, 800); '800' -> (800,); '200,800' -> (200, 800); a number or a list of numbers also works."""
    if isinstance(value, (int, float)):
        return (float(value),)
    if isinstance(value, (list, tuple)):
        return tuple(float(v) for v in value)
    v = str(value).strip().lower()
    if v in ('', 'auto'):
        return (200.0, 800.0)
    out = tuple(float(t) for t in v.replace(' ', '').split(',') if t)
    if not out or any(b <= 0 for b in out):
        raise ValueError('baud must be "auto", a number, or a comma separated list (got %r)' % (value,))
    return out
