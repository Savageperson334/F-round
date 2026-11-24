// u16
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/lrrybackup.js, line 56
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const u16 = (b, o) => b[o] | b[o + 1] << 8;
