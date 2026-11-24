// paramMessage
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/dx7.js, line 109
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function paramMessage(p, value) {
  return [0xf0, 0x43, 0x10, (p >> 7) & 0x7f, p & 0x7f, value & 0x7f, 0xf7];
}
