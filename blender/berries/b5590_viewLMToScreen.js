// viewLMToScreen
//
// Copied verbatim from https://github.com/ovro-lwa/astrowidget
//   file js/projection.js, line 157
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function viewLMToScreen(l, m, scaleX, scaleY, rotationRad = 0) {
  let l0 = l;
  let m0 = m;
  if (rotationRad !== 0) {
    const c = Math.cos(rotationRad);
    const s = Math.sin(rotationRad);
    l0 = l * c - m * s;
    m0 = l * s + m * c;
  }
  return { x: -l0 / scaleX, y: m0 / scaleY };
}
