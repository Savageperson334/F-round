// compactStep
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/patslot.js, line 19
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function compactStep(b) {
  const n = b[4] & 7, vel = b[5] & 127, prob = b[8] & 127;
  let nd = 0, c = 0;
  for (let j = 0; j < 4; j++) { nd |= (b[j] >> 7) << j; if (b[j] & 127) c = j + 1; }
  const c0 = ((b[4] >> 3) & 3) | ((b[4] >> 5) & 3) << 2 | ((b[5] >> 7) | (b[8] >> 7) << 1) << 4;
  if (!n && !c && !vel && !prob && !nd) return [c0];
  if (n === 1 && c === 1 && !nd && !prob) return [c0 | 1 << 6, b[0] & 127, vel];
  const out = [c0 | 2 << 6, n | c << 3, vel, prob, nd]; for (let j = 0; j < c; j++) out.push(b[j] & 127);
  return out;
}
