// easeOutQuad
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/core.js, line 143
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const DEFAULT_MIN = 0;

const DEFAULT_MAX = 1;


const clamp = (value, min = DEFAULT_MIN, max = DEFAULT_MAX) => Math.max(min, Math.min(max, value));


const easeOutQuad = (progress) => {
  const clamped = clamp(progress);
  return clamped * (2 - clamped);
};
