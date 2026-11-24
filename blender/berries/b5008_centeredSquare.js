// centeredSquare
//
// Copied verbatim from https://github.com/experimentalDataAesthetics/play-splom
//   file app/utils/layout.js, line 51
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function centeredSquare(width, height) {
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
    position: 'absolute',
    left: widthMargin,
    right: width - widthMargin,
    width: innerLength,
    height: innerLength,
    top: 0,
    bottom: innerLength
  };
}
