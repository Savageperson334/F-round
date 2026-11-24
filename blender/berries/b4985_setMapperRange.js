// setMapperRange
//
// Copied verbatim from https://github.com/experimentalDataAesthetics/play-splom
//   file app/actions/mapping.js, line 108
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function setMapperRange(feature, param, range) {
  return {
    type: 'setMappingRange',
    payload: {
      feature,
      param,
      range
    }
  };
}
