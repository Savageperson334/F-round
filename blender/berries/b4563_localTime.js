// localTime
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/core.js, line 243
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const MIN_DURATION = 1e-9;

const DEFAULT_MIN = 0;

const DEFAULT_MAX = 1;


const clamp = (value, min = DEFAULT_MIN, max = DEFAULT_MAX) => Math.max(min, Math.min(max, value));


const norm = (time, start, end) => clamp((time - start) / Math.max(MIN_DURATION, end - start));


function localTime(time, start, end) {
  return { t: norm(time, start, end), seconds: time - start, duration: end - start };
}
