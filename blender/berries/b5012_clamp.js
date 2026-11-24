// clamp
//
// Copied verbatim from https://github.com/farizdotid/bumber-motion-text
//   file scripts/gen-sfx.js, line 11
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const clamp = (v) => Math.max(-1, Math.min(1, v));
