// clamp
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file app/web/emu/app.js, line 15
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const clamp = (v, lo, hi) => (v < lo ? lo : v > hi ? hi : v);
