// planetLabelColor
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/PlanetLabel.js, line 32
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function planetLabelColor(color) {
  return Number.isInteger(color) && color >= 0 && color <= 0xffffff
    ? `#${color.toString(16).padStart(6, "0")}`
    : null;
}
