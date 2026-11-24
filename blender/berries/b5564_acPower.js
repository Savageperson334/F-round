// acPower
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/wavetable.js, line 136
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const acPower = (f) => { let m = 0, q = 0; for (const x of f) { m += x; q += x * x; } m /= f.length; return q / f.length - m * m; };
