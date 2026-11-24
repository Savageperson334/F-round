// expectByte
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/test_wavetable.mjs, line 30
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const expectByte = (r) => (r > 0 ? Math.max(0, Math.round(255 + 16 * Math.log2(r))) : 0);
