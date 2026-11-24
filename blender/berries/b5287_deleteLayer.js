// deleteLayer
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/layer/layerActions.js, line 63
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const DELETE_LAYER = 'DELETE_LAYER';


const deleteLayer = (layerID) => {
    return {
        type: DELETE_LAYER,
        value: layerID
    };
};
