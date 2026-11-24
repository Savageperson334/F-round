// getFirstAndLastCoordsFromTempCoords
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/utils/drawingUtils.js, line 130
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const getFirstAndLastCoordsFromTempCoords = (coords) => {
    const first = coords[0];
    const last = coords[coords.length - 1];
    return [first, last];
};
