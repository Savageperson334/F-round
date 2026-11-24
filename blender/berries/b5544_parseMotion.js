// parseMotion
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 121
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rv14 = (a, o = 0) => ((a[o] | a[o + 1] << 7) - 8192);


function parseMotion(a, op8 = true, wide = true) {
  const count = op8 ? a[3] | a[4] << 7 : a[3], max = op8 ? a[5] | a[6] << 7 : a[4];
  let o = op8 ? 7 : 5; const rows = [];
  for (let i = 0; i < count; i++) rows.push({ step: a[o + 4 * i], tid: a[o + 4 * i + 1], v: rv14(a, o + 4 * i + 2), lock: false });
  o += 4 * count;
  if (a.length >= o + count) rows.forEach((r, i) => { r.lock = a[o + i] === 1; });
  o += count;
  if (wide && a.length >= o + count) rows.forEach((r, i) => { if (a[o + i] === 1) r.tid += 128; });
  return { track: a[0], rc: a[1], on: a[2], count, max, rows };
}
