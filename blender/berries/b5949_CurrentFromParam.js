// CurrentFromParam
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 175
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const kCurrentHigh = 1.5;


const clamp = (v, lo, hi) => (v < lo ? lo : hi < v ? hi : v);


const clamp01 = (v) => clamp(v, 0.0, 1.0);


const linear = (v, low, high) => low + (high - low) * clamp01(v);


const CurrentFromParam = (v) => linear(v, 0.0, kCurrentHigh);
