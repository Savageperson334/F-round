// airDensityMolM3
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/utils/concentrationUnits.js, line 30
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const GAS_CONSTANT = 8.31446261815324


function airDensityMolM3(pressurePa, temperatureK) {
  return pressurePa / (GAS_CONSTANT * temperatureK)
}
