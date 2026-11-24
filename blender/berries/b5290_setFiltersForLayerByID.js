// setFiltersForLayerByID
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/layer/layerActions.js, line 86
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_FILTERS_FOR_LAYER_BY_ID = 'SET_FILTERS_FOR_LAYER_BY_ID';


const setFiltersForLayerByID = (layerID, filters) => {
    return {
        type: SET_FILTERS_FOR_LAYER_BY_ID,
        value: { layerID, filters }
    };
};
