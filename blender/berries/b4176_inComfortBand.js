// inComfortBand
//
// Copied verbatim from https://github.com/Chienlin1014/Orrery
//   file orrery.js, line 141
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const COMFORT_BAND = { minSeconds: 8, maxSeconds: 40 };


function inComfortBand(seconds) {
  return seconds >= COMFORT_BAND.minSeconds && seconds <= COMFORT_BAND.maxSeconds;
}
