// answer
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/fm1flash.js, line 111
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


function answer(type, addr, data) {
  const n = data.length, body = n + 8;
  const msg = [0x00, 0x59, 0x30, body & 255, (body >> 8) & 255, (body >> 16) & 255, type,
    addr & 255, (addr >>> 8) & 255, (addr >>> 16) & 255, (addr >>> 24) & 255, n & 255, (n >> 8) & 255, (n >> 16) & 255];
  for (const b of data) msg.push(b);
  let sum = 0;
  for (let i = 6; i < msg.length; i++) sum += msg[i];
  msg.push(~sum & 255);
  return [0xf0, ...to7(msg), 0xf7];
}
