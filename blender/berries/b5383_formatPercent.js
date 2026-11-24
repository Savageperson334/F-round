// formatPercent
//
// Copied verbatim from https://github.com/microsoft/haste
//   file ui/src/util/assessmentSummary.js, line 1
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const formatPercent = (value) =>
  value == null ? "—" : `${(value * 100).toFixed(1)}%`;
