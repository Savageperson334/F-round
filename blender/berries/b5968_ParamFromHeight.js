// ParamFromHeight
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 203
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const kHeightLow = 0.02;

const kHeightHigh = 1.0;

const f32 = Math.fround;


const min2 = (a, b) => (b < a ? b : a);


const max2 = (a, b) => (a < b ? b : a);


const clamp = (v, lo, hi) => (v < lo ? lo : hi < v ? hi : v);


function inverseGeometric(value, low, high) {
  const lo = min2(low, high);
  const hi = max2(low, high);
  return f32(Math.log(clamp(value, lo, hi) / low) / Math.log(high / low));
}


const ParamFromHeight = (m) => inverseGeometric(m, kHeightLow, kHeightHigh);
