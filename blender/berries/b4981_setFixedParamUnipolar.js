// setFixedParamUnipolar
//
// Copied verbatim from https://github.com/experimentalDataAesthetics/play-splom
//   file app/actions/mapping.js, line 42
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function setFixedParamUnipolar(param, value) {
  return {
    type: 'setFixedParam',
    payload: {
      param,
      values: {
        value
      }
    }
  };
}
