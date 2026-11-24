// resolveViewScales
//
// Copied verbatim from https://github.com/ovro-lwa/astrowidget
//   file js/projection.js, line 116
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function viewFovAxes(viewFov, aspect) {
  let fovWidth, fovHeight;
  if (aspect >= 1) {
    fovWidth = viewFov;
    fovHeight = viewFov / aspect;
  } else {
    fovHeight = viewFov;
    fovWidth = viewFov * aspect;
  }
  return {
    fovWidth,
    fovHeight,
    scaleX: Math.sin(fovWidth * 0.5),
    scaleY: Math.sin(fovHeight * 0.5),
  };
}


function resolveViewScales(viewFov, aspect, scales) {
  if (scales?.scaleX > 0 && scales?.scaleY > 0) return scales;
  return viewFovAxes(viewFov, aspect);
}
