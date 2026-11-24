// money
//
// Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
//   file legacy_library/server.js, line 86
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Archaeology & digital heritage
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function money(cents) {
  return (cents / 100).toFixed(2);
}
