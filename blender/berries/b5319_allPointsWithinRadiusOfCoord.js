// allPointsWithinRadiusOfCoord
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/utils/lineUtils.js, line 188
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const allPointsWithinRadiusOfCoord = (centerX, centerY, radius) => {
    const points = [[centerX, centerY]];
    for (let x = centerX - radius; x <= centerX; x += 1) {
        for (let y = centerY - radius; y <= centerY; y += 1) {
            if (
                (x - centerX) * (x - centerX) + (y - centerY) * (y - centerY) <
                radius * radius
            ) {
                points.push([x, y]);
            }
        }
    }
    return points;
};
