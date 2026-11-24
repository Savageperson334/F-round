// from7
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/fm1flash.js, line 63
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function from7(bytes) {
  const out = []; let acc = 0, bits = 0;
  for (const b of bytes) {
    acc |= (b & 0x7f) << bits; bits += 7;
    while (bits >= 8) { out.push(acc & 0xff); acc >>>= 8; bits -= 8; }
  }
  return out;
}
