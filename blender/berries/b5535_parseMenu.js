// parseMenu
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 83
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rv14 = (a, o = 0) => ((a[o] | a[o + 1] << 7) - 8192);


function rstr(a, pos) { let s = ""; while (pos < a.length && a[pos]) s += String.fromCharCode(a[pos++]); return [s, pos + 1]; }


function parseMenu(a) {                      // index, id, kind, value, min, max, name, names|unit, tab, tabname
  if (a[1] === 127) return null;
  const o = { index: a[0], id: a[1], kind: a[2], value: rv14(a, 3), min: rv14(a, 5), max: rv14(a, 7) };
  let pos = 9; [o.name, pos] = rstr(a, pos);
  if (o.kind === 0) { o.names = []; for (let i = 0; i <= o.max - o.min; i++) { const [s, n] = rstr(a, pos); o.names.push(s); pos = n; } }
  else if (o.kind === 1 || o.kind === 2) { [o.unit, pos] = rstr(a, pos); }   // 1: a number; 2 (0.2.22): a number in tenths of its unit (TUNE: 4400 = 440.0 Hz)
  if (pos < a.length) { o.tab = a[pos]; [o.tabName] = rstr(a, pos + 1); } else { o.tab = 0; o.tabName = ""; }
  return o;
}
