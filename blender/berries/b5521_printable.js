// printable
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/patslot.js, line 45
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const printable = (b, from, n) => { for (let i = 0; i < n; i++) if (b[from + i] < 32 || b[from + i] > 126) return false; return true; };
