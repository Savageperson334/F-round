// easeOutExpo
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/core.js, line 124
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const EXPO_DECAY = 10;

const DEFAULT_MIN = 0;

const DEFAULT_MAX = 1;


const clamp = (value, min = DEFAULT_MIN, max = DEFAULT_MAX) => Math.max(min, Math.min(max, value));


const easeOutExpo = (progress) => (
  progress === 1 ? 1 : 1 - Math.pow(2, -EXPO_DECAY * clamp(progress))
);
