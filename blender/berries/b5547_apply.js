// apply
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/roll.js, line 63
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const apply = (steps, ch) => { const o = steps.slice(); for (const [i, s] of ch) o[i] = s; return o; };
