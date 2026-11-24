// isPointArrayValid
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/utils/testUtils.js, line 46
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const isPointArrayValid = (pointArray) => {
    const invalidReasons = [];

    if (!Array.isArray(pointArray)) {
        invalidReasons.push('not array');
        return invalidReasons;
    }

    pointArray.forEach((points) => {
        if (points.length !== 2) {
            invalidReasons.push('length wrong');
        }

        const [x, y] = points;

        if (
            (x != null && typeof x !== 'number') ||
            (y != null && typeof y !== 'number')
        ) {
            invalidReasons.push('contains non-numbers');
        }

        if (x < 0 || y < 0) {
            invalidReasons.push('contains negative numbers');
        }
    });
    if (invalidReasons.length === 0) {
        return true;
    }
    return [...new Set(invalidReasons)];
};
