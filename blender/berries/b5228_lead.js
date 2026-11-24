// lead
//
// Copied verbatim from https://github.com/jb3/meeple
//   file web/audio/music.js, line 123
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Peculiar interfaces, worlds, visual systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const PERMS = (() => {
  const out = [];
  const rec = (a, rest) => {
    if (!rest.length) out.push(a);
    rest.forEach((x, i) => rec([...a, x], [...rest.slice(0, i), ...rest.slice(i + 1)]));
  };
  rec([], [0, 1, 2, 3]);
  return out;
})();


function lead(prev, pcs, lo, hi) {
  let best = null;
  let cost = Infinity;
  for (const perm of PERMS) {
    let c = 0;
    const notes = [];
    for (let v = 0; v < 4; v++) {
      let d = (((pcs[perm[v]] - prev[v]) % 12) + 12) % 12;
      if (d > 6) d -= 12;
      let n = prev[v] + d;
      while (n > hi) n -= 12;
      while (n < lo) n += 12;
      c += Math.abs(n - prev[v]);
      notes.push(n);
    }
    // two voices on one pitch would just thin the chord
    c += (4 - new Set(notes).size) * 30;
    if (c < cost) {
      cost = c;
      best = notes;
    }
  }
  return best.sort((a, b) => a - b);
}
