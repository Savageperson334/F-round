// formatBytes
//
// Copied verbatim from https://github.com/romainguy/adrift
//   file web/js/app.js, line 537
//   licence (as GitHub reports it): MPL-2.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatBytes(bytes) {
  if (!bytes) return '';
  return `${Math.round(bytes / 1024)} KB`;
}
