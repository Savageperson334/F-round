// normVer
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/fwcards.js, line 27
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const normVer = (v) => String(v || "").trim().replace(/^v/i, "").toLowerCase();
