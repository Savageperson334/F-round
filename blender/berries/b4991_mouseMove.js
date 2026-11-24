// mouseMove
//
// Copied verbatim from https://github.com/experimentalDataAesthetics/play-splom
//   file app/actions/ui.js, line 39
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function mouseMove(event) {
  // only need x / y and
  return {
    type: 'mouseMove',
    payload: event
  };
}
