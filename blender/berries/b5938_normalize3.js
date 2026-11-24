// normalize3
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/viewFit.js, line 83
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function hypot3(v) { return Math.hypot(v[0], v[1], v[2]); }


function normalize3(v) {
  const mag = hypot3(v);
  return mag > 1e-8 ? [v[0] / mag, v[1] / mag, v[2] / mag] : null;
}
