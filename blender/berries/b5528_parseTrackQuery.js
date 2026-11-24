// parseTrackQuery
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 41
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rv14 = (a, o = 0) => ((a[o] | a[o + 1] << 7) - 8192);


function parseTrackQuery(a, ntrk = 4) {      // TRACK reply: selected, NTRK, per track: engine, preset, level v14, mute, armed
  const out = { selected: a[0], tracks: [] };
  for (let t = 0; t < Math.min(a[1], ntrk); t++) { const o = 2 + t * 6; out.tracks.push({ eng: a[o], preset: a[o + 1], level: rv14(a, o + 2), mute: a[o + 4], armed: a[o + 5] }); }
  return out;
}
