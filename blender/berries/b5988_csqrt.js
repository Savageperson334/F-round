// csqrt
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 362
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const max2 = (a, b) => (a < b ? b : a);


function csqrt(z) {
  const r = Math.hypot(z[0], z[1]);
  const re = Math.sqrt(max2(0.5 * (r + z[0]), 0.0));
  const im = Math.sqrt(max2(0.5 * (r - z[0]), 0.0));
  return [re, z[1] < 0.0 ? -im : im];
}
