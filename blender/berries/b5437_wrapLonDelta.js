// wrapLonDelta
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 431
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function wrapLonDelta(lon, centerLon) {
  let d = ((lon - centerLon + 180) % 360 + 360) % 360 - 180;
  return d;
}
