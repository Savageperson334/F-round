// getDistance
//
// Copied verbatim from https://github.com/jun-mitani/orirevo
//   file orirevo_util.js, line 172
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function getDistance(x0, y0, x1, y1) {
  if (x1 == undefined) {
    return Math.sqrt( (x0.x - y0.x) * (x0.x - y0.x) + (x0.y - y0.y) * (x0.y - y0.y));
  } else {
    return Math.sqrt( (x0-x1) *(x0-x1) + (y0-y1)*(y0-y1));
  }
}
