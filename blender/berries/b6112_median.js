// median
//
// Copied verbatim from https://github.com/wangsquirrel/earth_motion
//   file scripts/benchmark-live-bodies.mjs, line 246
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function median(values) {
  const ordered = [...values].sort((a, b) => a - b);
  return ordered[Math.floor(ordered.length / 2)];
}
