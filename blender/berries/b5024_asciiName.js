// asciiName
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file app/site/manager/library.js, line 51
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const asciiName = text => [...text.normalize('NFKD').replace(/[̀-ͯ]/g,'')].map(c=>c>=' '&&c<='~'?c:'?').join('').slice(0,23);
