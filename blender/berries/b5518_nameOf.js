// nameOf
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/patchrecord.js, line 90
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const nameOf = (b, o) => { let s = ""; for (let i = 0; i < 12 && b[o + i]; i++) s += String.fromCharCode(b[o + i]); return s; };
