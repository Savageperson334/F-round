// isPow2
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/wavetable.js, line 139
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const isPow2 = (n) => n > 0 && !(n & (n - 1));
