// ascii
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file tools/make_factory500.mjs, line 21
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const ascii=s=>s.normalize('NFKD').replace(/[\u0300-\u036f]/g,'').replace(/[“”]/g,'"').replace(/[‘’]/g,"'").replace(/[^\x20-\x7e]/g,'?');
