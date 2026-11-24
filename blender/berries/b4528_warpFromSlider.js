// warpFromSlider
//
// Copied verbatim from https://github.com/TerjeRu/orrery
//   file ui/src/time-control.js, line 27
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const WARP_SLIDER_MAX = 100;


function warpFromSlider(sliderValue) {
  return Math.round(10 ** (sliderValue / (WARP_SLIDER_MAX / 5)));
}
