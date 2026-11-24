// centeredSquareMargin
//
// Copied verbatim from https://github.com/experimentalDataAesthetics/play-splom
//   file app/utils/layout.js, line 1
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function centeredSquareMargin(width, height) {
  const innerLength = Math.min(width, height);
  let widthMargin = width - innerLength;
  if (widthMargin > 0) {
    widthMargin /= 2;
  }

  let heightMargin = height - innerLength;
  if (heightMargin) {
    heightMargin /= 2;
  }

  return {
    margin: `0 ${widthMargin}px ${heightMargin}px`,
    width: `${innerLength}px`,
    height: `${innerLength}px`
  };
}
