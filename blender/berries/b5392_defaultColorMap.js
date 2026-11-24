// defaultColorMap
//
// Copied verbatim from https://github.com/mikolalysenko/orthogami
//   file index.js, line 38
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

var palette = [
  'magenta',
  'blue',
  'green',
  'purple',
  'gold',
  'red',
  'bisque',
  'brown',
  'darkblue',
  'goldenrod',
  'aquamarine',
  'white',
  'black'
]


function defaultColorMap(v) {
  return palette[(v>>>0)%palette.length]
}
