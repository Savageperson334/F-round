// inverseLinear
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 152
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const f32 = Math.fround;


const clamp = (v, lo, hi) => (v < lo ? lo : hi < v ? hi : v);


const inverseLinear = (value, low, high) => f32(clamp((value - low) / (high - low), 0.0, 1.0));
