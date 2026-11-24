// naturalKey
//
// Copied verbatim from https://github.com/marksweiss/tastywaves
//   file tools/web/convert.js, line 186
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function naturalKey(s) { return s.toLowerCase().split(/(\d+)/).map((t, i) => i % 2 ? +t : t); }
