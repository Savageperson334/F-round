// deleteFillLinesFromLayerByID
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/line/lineActions.js, line 36
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const DELETE_FILL_LINES_FROM_LAYER_BY_ID =
    'DELETE_FILL_LINES_FROM_LAYER_BY_ID';


const deleteFillLinesFromLayerByID = (layerID, fillLines, inside) => {
    return {
        type: DELETE_FILL_LINES_FROM_LAYER_BY_ID,
        value: { layerID, fillLines, inside }
    };
};
