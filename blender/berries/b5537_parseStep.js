// parseStep
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 97
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function parseStep(a, o = 0) {               // index, n, note0..3, time, flags, vel, hits(3), chance, ratchet, nudge+8   (offset o skips a track byte)
  return { index: a[o], n: a[o + 1], notes: a.slice(o + 2, o + 6), time: a[o + 6], flags: a[o + 7], vel: a[o + 8], hits: a.slice(o + 9, o + 12), chance: a[o + 12] ?? 100, ratchet: a[o + 13] ?? 1, nudge: a[o + 14] ?? 8 };
}
