// formatSeconds
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/cue-model.js, line 203
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatSeconds(value, decimals = 3) {
  if (value === null || !Number.isFinite(value)) return '—';
  return value.toFixed(decimals);
}
