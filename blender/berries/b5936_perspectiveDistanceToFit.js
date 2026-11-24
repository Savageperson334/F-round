// perspectiveDistanceToFit
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/viewFit.js, line 73
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function perspectiveDistanceToFit(radius, fovDeg, aspect, zoom = 1) {
  const halfV = (fovDeg * Math.PI / 180) / 2;
  const halfH = Math.atan(Math.tan(halfV) * Math.max(aspect, 1e-6));
  const half = Math.min(halfV, halfH);
  if (!(half > 0) || !(radius > 0)) return null;
  return (radius / Math.tan(half)) * Math.max(zoom, 1e-6);
}
