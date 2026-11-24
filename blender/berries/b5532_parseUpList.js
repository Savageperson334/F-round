// parseUpList
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 64
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function rstr(a, pos) { let s = ""; while (pos < a.length && a[pos]) s += String.fromCharCode(a[pos++]); return [s, pos + 1]; }


function parseUpList(a) {
  const start = a[0], count = a[1], total = a[2], slots = []; let pos = 3;
  for (let i = 0; i < count; i++) { const used = a[pos], eng = a[pos + 1]; const [name, n] = rstr(a, pos + 2); pos = n; slots.push({ slot: start + i, used: !!used, eng, name }); }
  slots.forEach((s, i) => { s.cat = a[pos + i] ?? 0; });
  const hasSaved = a.length >= pos + 2 * count;
  slots.forEach((s, i) => { s.saved = hasSaved ? !!a[pos + count + i] : s.used; });
  return { start, count, total, slots };
}
