// FluidOf
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 282
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const kMu0 = 1.25663706212e-6;

const DATASHEETS = [
  { name: 'EFH1', density: 1210.0, tension: 0.029, viscosity: 6.0e-3, chi: 2.58, saturation: 0.044 / kMu0 },
  { name: 'EMG 901', density: 1530.0, tension: 0.0295, viscosity: 10.0e-3, chi: 1.3, saturation: 4.8e4 },
  { name: 'EMG 909', density: 1020.0, tension: 0.0265, viscosity: 6.0e-3, chi: 0.8, saturation: 1.6e4 },
];


const clamp = (v, lo, hi) => (v < lo ? lo : hi < v ? hi : v);


const FluidOf = (id) => DATASHEETS[clamp(id, 0, DATASHEETS.length - 1)];
