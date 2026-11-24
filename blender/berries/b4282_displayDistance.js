// displayDistance
//
// Copied verbatim from https://github.com/MizarWeb/Mizar
//   file examples/getting-started-bing.js, line 15
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function displayDistance(distance) {
  var value;
  if (distance >= 10000) {
    distance = distance / 1000;
    value = distance.toFixed(2) + "km";
  } else {
    value = distance + "m";
  }
  return value;
}
