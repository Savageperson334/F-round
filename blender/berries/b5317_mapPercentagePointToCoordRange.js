// mapPercentagePointToCoordRange
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/utils/FilterUtils.js, line 14
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const mapPercentagePointToCoordRange = (
    coordMin,
    coordMax,
    percentage
) => {
    return (percentage * (coordMax - coordMin)) / 100 + coordMin;
};
