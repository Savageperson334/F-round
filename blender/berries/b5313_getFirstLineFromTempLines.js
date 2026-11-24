// getFirstLineFromTempLines
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/utils/drawingUtils.js, line 122
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const getFirstLineFromTempLines = (tempLines) => {
    if (tempLines[0] == null) {
        return false;
    }

    return [...tempLines[0]];
};
