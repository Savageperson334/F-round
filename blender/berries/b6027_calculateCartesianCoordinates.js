// calculateCartesianCoordinates
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/utils.js, line 115
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function multiplyMatrixVector(matrix, vector) {
  const result = [];
  for (let i = 0; i < matrix.length; i++) {
    let sum = 0;
    for (let j = 0; j < matrix[i].length; j++) {
      sum += matrix[i][j] * vector[j];
    }
    result.push(sum);
  }

  return result;
}


function calculateCartesianCoordinates(matrix, fractionalCoordinates) {
  // transpose the matrix
  matrix = matrix[0].map((_, colIndex) => matrix.map((row) => row[colIndex]));
  return multiplyMatrixVector(matrix, fractionalCoordinates);
}
