// checksum
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/dx7.js, line 125
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function checksum(bytes) {
  let s = 0;
  for (const b of bytes) s += b;
  return (128 - (s & 0x7f)) & 0x7f;
}
