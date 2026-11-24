// radarPoint
//
// Copied verbatim from https://github.com/TonoT/paleontology
//   file src/main.js, line 94
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Fossil measurements and paleontology
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function radarPoint(value, index, radius = 82) {
  const angle = (-90 + index * 60) * Math.PI / 180;
  const distance = radius * value / 100;
  return `${100 + Math.cos(angle) * distance},${100 + Math.sin(angle) * distance}`;
}
