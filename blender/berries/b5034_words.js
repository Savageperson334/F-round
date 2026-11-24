// words
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file tools/factory_pick.mjs, line 15
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const words = name => name.replace(/([a-z])([A-Z])/g, '$1 $2').toUpperCase().replace(/[^A-Z]+/g, ' ').trim();
