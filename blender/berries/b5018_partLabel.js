// partLabel
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file app/site/manager/app.js, line 327
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const partLabel = (mode, p) => mode === 2 ? String(p + 1) : 'LR'[p];
