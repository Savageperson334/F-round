// easeOutElastic
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/core.js, line 153
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ELASTIC_PERIOD = 0.3;

const EXPO_DECAY = 10;

const DEFAULT_MIN = 0;

const DEFAULT_MAX = 1;


const clamp = (value, min = DEFAULT_MIN, max = DEFAULT_MAX) => Math.max(min, Math.min(max, value));


const easeOutElastic = (progress) => {
  const clamped = clamp(progress);
  if (clamped === 0 || clamped === 1) return clamped;
  const scale = (2 * Math.PI) / ELASTIC_PERIOD;
  return (Math.pow(2, -EXPO_DECAY * clamped) * Math.sin((clamped - ELASTIC_PERIOD / 4) * scale)) + 1;
};
