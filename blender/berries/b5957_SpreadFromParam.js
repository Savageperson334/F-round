// SpreadFromParam
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 187
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const kSpreadLow = 0.02;

const kSpreadHigh = 0.10;


const clamp = (v, lo, hi) => (v < lo ? lo : hi < v ? hi : v);


const clamp01 = (v) => clamp(v, 0.0, 1.0);


const geometric = (v, low, high) => low * Math.pow(high / low, clamp01(v));


const SpreadFromParam = (v) => geometric(v, kSpreadLow, kSpreadHigh);
