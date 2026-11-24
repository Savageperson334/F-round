// fromKelvin
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/components/Plots/temperatureUnits.js, line 13
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fromKelvin(kelvin, unitId) {
  if (unitId === 'C') return kelvin - 273.15
  if (unitId === 'F') return ((kelvin - 273.15) * 9) / 5 + 32
  return kelvin
}
