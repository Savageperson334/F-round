// screenToViewLM
//
// Copied verbatim from https://github.com/ovro-lwa/astrowidget
//   file js/projection.js, line 135
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function screenToViewLM(x, y, scaleX, scaleY, rotationRad = 0) {
  const l0 = -x * scaleX;
  const m0 = y * scaleY;
  if (rotationRad === 0) return { l: l0, m: m0 };
  const c = Math.cos(rotationRad);
  const s = Math.sin(rotationRad);
  return {
    l: l0 * c + m0 * s,
    m: -l0 * s + m0 * c,
  };
}
