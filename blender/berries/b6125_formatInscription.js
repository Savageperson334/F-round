// formatInscription
//
// Copied verbatim from https://github.com/wikisocph/eph-historical-markers-map
//   file js/eph-historical-markers.js, line 658
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatInscription(text) {
  return '<p>' + text.replace(/\s*<br\s*\/?>\s*<br\s*\/?>\s*/gi, '</p><p>') + '</p>';
}
