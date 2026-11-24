// parseTags
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/app.js, line 1258
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const parseTags = (s) => [...new Set(String(s).split(/[\s,]+/).map((t) => t.replace(/^#+/, "").trim().slice(0, 64)).filter(Boolean))];
