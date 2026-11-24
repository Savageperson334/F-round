// loadProject
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/rootActions.js, line 11
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const LOAD_PROJECT = 'LOAD_PROJECT';


const loadProject = (projectState) => {
    return {
        type: LOAD_PROJECT,
        value: projectState
    };
};
