// wherePoints
//
// Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
//   file web/app.js, line 1128
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const wherePoints = m => Math.round(100 * Math.exp(-m / 450));
