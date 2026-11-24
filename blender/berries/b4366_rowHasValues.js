// rowHasValues
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/conditions/table.js, line 212
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const isFiniteNumber = (value) => typeof value === 'number' && Number.isFinite(value)


function rowHasValues(columns, index) {
  return columns.some((values) => isFiniteNumber(values?.[index]))
}
