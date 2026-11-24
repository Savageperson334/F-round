// parseUpGet
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 73
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function rstr(a, pos) { let s = ""; while (pos < a.length && a[pos]) s += String.fromCharCode(a[pos++]); return [s, pos + 1]; }


const rv14 = (a, o = 0) => ((a[o] | a[o + 1] << 7) - 8192);


function parseUpGet(a, pcount) {
  const [name, p0] = rstr(a, 3); let pos = p0;
  const values = []; for (let i = 0; i < pcount; i++, pos += 2) values.push(rv14(a, pos));
  const notes = []; for (let i = 0; i < 16; i++, pos += 2) notes.push([a[pos], a[pos + 1]]);
  pos++;                                           // kind
  return { slot: a[0], used: !!a[1], eng: a[2], name, values, notes, cat: a[pos] ?? 0, saved: a[pos + 1] == null ? !!a[1] : !!a[pos + 1] };
}
