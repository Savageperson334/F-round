// modelOf
//
// Copied verbatim from https://github.com/romainguy/adrift
//   file web/js/flasher.js, line 301
//   licence (as GitHub reports it): MPL-2.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function modelOf(text) {
  const head = String(text).split('_')[0];
  return head.replace(/^ota-/i, '');
}
