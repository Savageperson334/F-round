// lerp3
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/viewFit.js, line 28
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function lerp(a, b, t) {
  return a + (b - a) * t;
}


function lerp3(a, b, t) {
  return [lerp(a[0], b[0], t), lerp(a[1], b[1], t), lerp(a[2], b[2], t)];
}
