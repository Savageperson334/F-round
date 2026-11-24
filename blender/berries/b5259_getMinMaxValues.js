// getMinMaxValues
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/components/Drawing/modes/text.mode.js, line 10
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const getMinMaxValues = (polygon) => {
    const xValues = polygon.map((arr) => arr[0]);
    const yValues = polygon.map((arr) => arr[1]);
    const minX = Math.min(...xValues);
    const maxX = Math.max(...xValues);
    const minY = Math.min(...yValues);
    const maxY = Math.max(...yValues);

    return {
        minX,
        maxX,
        minY,
        maxY
    };
};
