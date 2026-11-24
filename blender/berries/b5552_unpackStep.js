// unpackStep
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/stored.js, line 133
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function unpackStep(b, index) {
  let nd = 0; const notes = [];
  for (let j = 0; j < 4; j++) { nd |= (b[j] >> 7) << j; notes.push(b[j] & 127); }
  const r = (b[5] >> 7) | (b[8] >> 7) << 1;
  return { index, n: b[4] & 7, notes, time: (b[4] >> 3) & 3, flags: (b[4] >> 5) & 3, vel: b[5] & 127, hits: [0, 0, 0], chance: b[8] & 127, ratchet: r + 1, nudge: ((nd ^ 8) - 8) + 8 };
}
