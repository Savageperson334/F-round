# mark
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file tools/make_mark.py, line 97
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

AGENTS = [
    # x,     y,      r,    gaze x, gaze y
    (16.00, 16.00, 5.20, 0.00, 0.00),      # the middle one looks straight out
    (16.00, 5.70, 3.40, 0.00, 1.00),
    (25.80, 12.82, 3.40, -1.00, 0.16),
    (22.05, 24.33, 3.40, -0.72, -0.69),
    (9.95, 24.33, 3.40, 0.72, -0.69),
    (6.20, 12.82, 3.40, 1.00, -0.04),
]

LINKS = [
    ((16.00, 16.00), (22.05, 24.33)),      # the bar, out to five o'clock
    ((22.05, 24.33), (9.95, 24.33)),       # five to seven
    ((9.95, 24.33), (6.20, 12.82)),        # seven to ten
    ((6.20, 12.82), (16.00, 5.70)),        # ten to twelve
    ((16.00, 5.70), (25.80, 12.82)),       # twelve to two, and stop
]

GAZE_SHARE = 0.15

IRIS_INK = "#5ab6ef"

IRIS_SHARE = 0.60

PUPIL_INK = "#05070a"

PUPIL_SHARE = 0.31

SPOKES = 9


def eye(x: float, y: float, r: float, gx: float, gy: float) -> list[str]:
    """One eye: an iris, spokes running out from the centre, and a pupil."""
    cx = x + gx * r * GAZE_SHARE
    cy = y + gy * r * GAZE_SHARE
    iris = r * IRIS_SHARE
    pupil = r * PUPIL_SHARE

    out = [f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{iris:.2f}" '
           f'fill="{IRIS_INK}"/>']

    # Spokes, so the iris has some structure to it rather than being a flat
    # disc. Started clear of the pupil and stopped short of the rim.
    inner, outer = pupil * 1.12, iris * 0.94
    spokes = []
    for k in range(SPOKES):
        angle = (k / SPOKES) * math.tau + 0.2
        spokes.append(
            f'M{cx + math.cos(angle) * inner:.2f} {cy + math.sin(angle) * inner:.2f}'
            f'L{cx + math.cos(angle) * outer:.2f} {cy + math.sin(angle) * outer:.2f}')
    out.append(f'<path d="{" ".join(spokes)}" stroke="{PUPIL_INK}" '
               f'stroke-width="{r * 0.075:.2f}" opacity="0.30" fill="none"/>')

    out.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{pupil:.2f}" fill="{PUPIL_INK}"/>')
    return out


def mark(colour: str, indent: str) -> str:
    """The whole mark, in whatever colour it is asked for."""
    pad = "\n" + indent
    links = " ".join(f"M{a[0]:.2f} {a[1]:.2f}L{b[0]:.2f} {b[1]:.2f}" for a, b in LINKS)

    parts = [
        f'<g stroke="{colour}" stroke-width="1.4" fill="none" '
        f'stroke-linecap="round" opacity="0.5">',
        f'  <path d="{links}"/>',
        '</g>',
        f'<g fill="{colour}">',
    ]
    for x, y, r, _, _ in AGENTS:
        parts.append(f'  <circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}"/>')
    parts.append('</g>')
    for agent in AGENTS:
        parts.extend(eye(*agent))
    return pad.join(parts)
