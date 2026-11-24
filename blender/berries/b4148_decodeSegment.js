// decodeSegment
//
// Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
//   file legacy_library/server.js, line 105
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Archaeology & digital heritage
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function decodeSegment(segment) {
  try {
    return decodeURIComponent(segment);
  } catch (err) {
    return segment;
  }
}
