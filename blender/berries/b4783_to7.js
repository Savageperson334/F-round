// to7
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/fm1flash.js, line 54
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function to7(bytes) {
  const out = []; let acc = 0, bits = 0;
  for (const b of bytes) {
    acc |= b << bits; bits += 8;
    while (bits >= 7) { out.push(acc & 0x7f); acc >>>= 7; bits -= 7; }
  }
  if (bits) out.push(acc & 0x7f);
  return out;
}
