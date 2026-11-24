// showBrush
//
// Copied verbatim from https://github.com/experimentalDataAesthetics/play-splom
//   file app/actions/interaction.js, line 3
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function showBrush(show, x, y) {
  return {
    type: 'showBrush',
    payload: {
      show,
      x,
      y
    }
  };
}
