// getFillColor
//
// Copied verbatim from https://github.com/OnTheLine/otl-town-borders
//   file script.js, line 11
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function getFillColor(d) {
  return  d == 1 ? 'red' :
          d == 2 ? 'blue' :
          d == 3 ? 'green' :
          d == 4 ? 'white' :
          'white';
}
