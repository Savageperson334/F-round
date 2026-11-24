// parseLengthMm
//
// Copied verbatim from https://github.com/KilledByAPixel/VirtualPlotter
//   file code/plotExtract.js, line 23
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function parseLengthMm(s) {
  if (!s) return null;
  const m = String(s).trim().match(/^(-?[\d.eE+-]+)\s*([a-z%]*)$/i);
  if (!m) return null;
  const n = parseFloat(m[1]);
  if (!isFinite(n)) return null;
  const u = (m[2] || 'px').toLowerCase();
  const conv = { mm:1, cm:10, m:1000, in:25.4, pt:25.4/72, pc:25.4/6, px:25.4/96 };
  return n * (conv[u] ?? 25.4/96);
}
