// fail
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/fm1flash.js, line 49
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fail(code, message) { return Object.assign(new Error(message), { code }); }
