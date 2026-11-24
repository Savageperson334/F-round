// OptionIndex
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 208
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const clamp = (v, lo, hi) => (v < lo ? lo : hi < v ? hi : v);


const lround = (v) => (v < 0 ? -Math.round(-v) : Math.round(v));


const OptionIndex = (value, count) => clamp(lround(value), 0, count - 1);
