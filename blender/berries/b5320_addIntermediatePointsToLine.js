// addIntermediatePointsToLine
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/utils/lineUtils.js, line 214
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const addIntermediatePointsToLine = (line, passes = 1) => {
    let copiedLine = [...line];
    const onePass = (activeLine) => {
        const tempLine = [];
        activeLine.forEach(([currentX, currentY], index) => {
            tempLine.push([currentX, currentY]);
            if (activeLine[index + 1] != null) {
                const [nextX, nextY] = activeLine[index + 1];
                const midX = (currentX + nextX) / 2;
                const midY = (currentY + nextY) / 2;
                tempLine.push([midX, midY]);
            }
        });
        return tempLine;
    };

    for (let i = 0; i < passes; i++) {
        copiedLine = onePass(copiedLine);
    }
    return copiedLine;
};
