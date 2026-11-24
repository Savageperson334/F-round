// rgb
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/theme.js, line 7
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rgb = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
