// erasePointsAtCoords
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/line/lineActions.js, line 69
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ERASE_POINTS_WITHIN_ERASER_COORDS =
    'ERASE_POINTS_WITHIN_ERASER_COORDS';


const erasePointsAtCoords = (layerID, eraseCoords, eraserRadius) => {
    return {
        type: ERASE_POINTS_WITHIN_ERASER_COORDS,
        value: { layerID, eraseCoords, eraserRadius }
    };
};
