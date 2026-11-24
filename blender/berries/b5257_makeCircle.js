// makeCircle
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/components/Drawing/modes/circle.mode.js, line 3
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const makeCircle = (centerX, centerY, radius, pointsOnCircle = 50) => {
    const coords = [];
    for (let i = 0; i < pointsOnCircle; i += 1) {
        const thisX =
            centerX + radius * Math.cos((2 * Math.PI * i) / pointsOnCircle);
        const thisY =
            centerY + radius * Math.sin((2 * Math.PI * i) / pointsOnCircle);
        coords.push([thisX, thisY]);
    }
    const [first] = coords;
    return [...coords, first];
};
