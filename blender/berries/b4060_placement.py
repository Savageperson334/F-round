# placement
#
# Copied verbatim from https://github.com/ymatterlab/ycrystal
#   file src/ycrystal/core/background.py, line 134
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

FIT_MODES = ("fill", "fit")


def placement(
    width: int,
    height: int,
    frame_aspect: float,
    fit: str = "fill",
    zoom: float = 1.0,
    offset_x: float = 0.0,
    offset_y: float = 0.0,
) -> tuple[float, float, float, float]:
    """Return where a picture lies in the output frame: ``(cx, cy, w, h)``.

    Lengths are in units of the frame height; the frame spans ``±aspect/2`` in x and
    ``±1/2`` in y around its centre. The picture keeps its aspect ratio: ``"fit"``
    makes it as large as possible inside the frame, ``"fill"`` as small as possible
    while covering the frame; then `zoom` scales it about its centre, and the offsets
    move its centre by fractions of the frame width and height.

    Parameters
    ----------
    width, height
        Picture size in pixels.
    frame_aspect
        Output width / height.
    fit, zoom, offset_x, offset_y
        As in [`BackgroundImage`][ycrystal.core.background.BackgroundImage].

    Returns
    -------
    tuple of float
        Centre ``(cx, cy)`` and size ``(w, h)`` of the picture, with ``w / h`` equal to
        ``width / height``.
    """
    if width < 1 or height < 1 or not frame_aspect > 0:
        raise ValueError("picture size and frame aspect must be positive")
    if fit not in FIT_MODES:
        raise ValueError(f"fit must be one of {FIT_MODES}")
    ratio = width / height
    wider = ratio >= frame_aspect
    if (fit == "fit") == wider:  # fit a wide picture, or fill with a tall one: full width
        w, h = frame_aspect, frame_aspect / ratio
    else:
        w, h = ratio, 1.0
    return (offset_x * frame_aspect, offset_y, w * zoom, h * zoom)
