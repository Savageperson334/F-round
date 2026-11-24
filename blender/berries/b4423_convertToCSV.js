// convertToCSV
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive-client
//   file src/redux/actions/examples.js, line 58
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function convertToCSV(arr) {
  const csvRows = arr.map((row) => row.join(","));
  return csvRows.join("\n");
}
