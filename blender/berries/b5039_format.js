// format
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file tools/make_factory500.mjs, line 73
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const format=bytes=>[...bytes].map(n=>String(n)).join(',');
