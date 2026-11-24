// easeInOut
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/core.js, line 60
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const DEFAULT_MIN = 0;

const DEFAULT_MAX = 1;


const clamp = (value, min = DEFAULT_MIN, max = DEFAULT_MAX) => Math.max(min, Math.min(max, value));


const easeInOut = (progress) => {
  const clamped = clamp(progress);
  if (clamped < 0.5) return 4 * clamped * clamped * clamped;
  return 1 - (Math.pow(-2 * clamped + 2, 3) / 2);
};
