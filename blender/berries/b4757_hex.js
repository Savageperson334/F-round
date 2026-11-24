// hex
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/app.js, line 37
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const hex = (bytes) => [...bytes].map((b) => b.toString(16).padStart(2, "0").toUpperCase()).join(" ");
