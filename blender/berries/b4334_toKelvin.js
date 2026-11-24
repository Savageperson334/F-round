// toKelvin
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/components/Plots/temperatureUnits.js, line 7
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function toKelvin(value, unitId) {
  if (unitId === 'C') return value + 273.15
  if (unitId === 'F') return ((value - 32) * 5) / 9 + 273.15
  return value
}
