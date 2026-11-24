// lerp
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/viewFit.js, line 24
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function lerp(a, b, t) {
  return a + (b - a) * t;
}
