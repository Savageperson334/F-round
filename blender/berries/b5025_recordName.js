// recordName
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file app/site/manager/library.js, line 64
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function recordName(rec) {
  let t=''; for(let i=4;i<27&&rec[i];i++)t+=rec[i]>=32&&rec[i]<127?String.fromCharCode(rec[i]):'?'; return t;
}
