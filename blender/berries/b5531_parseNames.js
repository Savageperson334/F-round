// parseNames
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 56
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function rstr(a, pos) { let s = ""; while (pos < a.length && a[pos]) s += String.fromCharCode(a[pos++]); return [s, pos + 1]; }


function parseNames(a) {                     // engine, count, names..., two page titles
  const names = []; let pos = 2;
  for (let i = 0; i < a[1]; i++) { const [s, n] = rstr(a, pos); names.push(s); pos = n; }
  return { eng: a[0], names };
}
