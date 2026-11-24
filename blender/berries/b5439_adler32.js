// adler32
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 472
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function adler32(buf, offset, length) {
  let a = 1, b = 0;
  for (let i = offset; i < offset + length; i++) {
    a = (a + buf[i]) % 65521;
    b = (b + a) % 65521;
  }
  return ((b << 16) | a) >>> 0;
}
