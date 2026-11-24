// smooth
//
// Copied verbatim from https://github.com/jb3/meeple
//   file web/audio/core.js, line 57
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Peculiar interfaces, worlds, visual systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const smooth = (a, b, x) => {
  const t = Math.min(1, Math.max(0, (x - a) / (b - a)));
  return t * t * (3 - 2 * t);
};
