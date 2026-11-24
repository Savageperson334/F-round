// env
//
// Copied verbatim from https://github.com/farizdotid/bumber-motion-text
//   file scripts/gen-sfx.js, line 15
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const env = (t, dur, attack, curve = 3) => {
  if (t < attack) return t / attack;
  const d = (t - attack) / (dur - attack);
  return Math.pow(Math.max(0, 1 - d), curve);
};
