// lines
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file app/site/editor/patch.js, line 3
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function lines(bytes) {
  const result = [];
  for (let start = 0, i = 0; i <= bytes.length; i++) {
    if (i !== bytes.length && bytes[i] !== 10 && bytes[i] !== 13) continue;
    if (i > start || !result.length) result.push(bytes.slice(start,i));
    if (bytes[i] === 13 && bytes[i+1] === 10) i++;
    start = i+1;
  }
  return result;
}
