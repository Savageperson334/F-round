// getExtremePointsOfCoords
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/utils/plotUtils.js, line 89
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const getExtremePointsOfCoords = (flattenedCoords, radius = 0) => {
    const allXValues = flattenedCoords.map((pointArray) => pointArray[0]);
    const allYValues = flattenedCoords.map((pointArray) => pointArray[1]);

    const minX = Math.min(...allXValues) - radius;
    const maxX = Math.max(...allXValues) + radius;

    const minY = Math.min(...allYValues) - radius;
    const maxY = Math.max(...allYValues) + radius;

    return {
        minX,
        maxX,
        minY,
        maxY
    };
};
