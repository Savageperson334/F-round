// addDatasetPaths
//
// Copied verbatim from https://github.com/experimentalDataAesthetics/play-splom
//   file app/actions/datasets.js, line 119
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function addDatasetPaths(paths) {
  return {
    type: 'addDatasetPaths',
    payload: { paths }
  };
}
