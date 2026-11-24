// safePatchName
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/app.js, line 799
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const safePatchName = (s) => String(s || "").replace(/[^A-Za-z0-9 _.()\-]/g, "").replace(/^[^A-Za-z0-9]+/, "").slice(0, 64).trim();
