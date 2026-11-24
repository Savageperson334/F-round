// ParamFromNoise
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 194
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const f32 = Math.fround;

const kNoiseLow = 1e-6;

const kNoiseHigh = 1e-1;


const max2 = (a, b) => (a < b ? b : a);


const min2 = (a, b) => (b < a ? b : a);


const clamp = (v, lo, hi) => (v < lo ? lo : hi < v ? hi : v);


function inverseGeometric(value, low, high) {
  const lo = min2(low, high);
  const hi = max2(low, high);
  return f32(Math.log(clamp(value, lo, hi) / low) / Math.log(high / low));
}


const ParamFromNoise = (pa) => (pa <= 0.0 ? 0.0 : max2(f32(1e-6), inverseGeometric(pa, kNoiseLow, kNoiseHigh)));
