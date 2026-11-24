// opFreq
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/fm6edit.js, line 42
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function opFreq(mode, coarse, fine) {
  if (mode === 1) { const f = 10 ** (coarse & 3) * 10 ** (fine / 100); return `${f < 100 ? f.toFixed(2) : f.toFixed(0)} Hz`; }
  return `x ${((coarse || 0.5) * (1 + fine / 100)).toFixed(2)}`;
}
