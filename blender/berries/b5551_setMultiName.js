// setMultiName
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/stored.js, line 69
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function setMultiName(rec, name) { const r = rec.slice(); for (let i = 0; i < 12; i++) r[8 + i] = i < name.length ? name.charCodeAt(i) & 127 : 0; return r; }
