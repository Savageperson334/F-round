// deleteFilterFromLayer
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/layer/layerActions.js, line 111
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const DELETE_FILTER_FROM_LAYER = 'DELETE_FILTER_FROM_LAYER';


const deleteFilterFromLayer = (layerID, filterID) => {
    return {
        type: DELETE_FILTER_FROM_LAYER,
        value: { layerID, filterID }
    };
};
