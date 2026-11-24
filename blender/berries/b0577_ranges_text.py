# ranges_text
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/ssdv.py, line 63
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ranges_text(numbers):
    """[3, 5, 9, 10, 11] -> '3, 5, 9-11'"""
    out, run = [], []
    for n in sorted(numbers):
        if run and n == run[-1] + 1:
            run.append(n)
        else:
            if run:
                out.append(run)
            run = [n]
    if run:
        out.append(run)
    return ', '.join(str(r[0]) if len(r) == 1 else '%d-%d' % (r[0], r[-1]) for r in out)
