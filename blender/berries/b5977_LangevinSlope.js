// LangevinSlope
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 300
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function LangevinSlope(x) {
  const a = Math.abs(x);
  if (a < 1e-2) {
    const x2 = x * x;
    return 1.0 / 3.0 - x2 / 15.0 + (2.0 * x2 * x2) / 189.0;
  }
  if (a > 350.0) return 1.0 / (x * x);
  const s = Math.sinh(x);
  return 1.0 / (x * x) - 1.0 / (s * s);
}
