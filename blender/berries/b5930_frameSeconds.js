// frameSeconds
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/present.js, line 13
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const MAX_FRAME_SECONDS = 0.25;


function frameSeconds(previous, timestamp) {
  if (previous == null || !Number.isFinite(timestamp)) return 0;
  return Math.max(0, Math.min((timestamp - previous) / 1000, MAX_FRAME_SECONDS));
}
