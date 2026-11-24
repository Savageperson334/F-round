// makePercentage
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/utils/FilterUtils.js, line 1
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const makePercentage = (part, whole) => {
    return Math.floor((100 * part) / whole);
};
