// stringDiff
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file origami/src/dev/treeDot.js, line 179
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function stringDiff(first, second) {
  let i = 0;
  // Find point of first difference.
  while (i < first.length && i < second.length && first[i] === second[i]) {
    i++;
  }
  // Back up to start of that line.
  while (i > 0 && second[i - 1] !== "\n") {
    i--;
  }
  // Move forward to first non-whitespace character.
  while (i < second.length && /\s/.test(second[i])) {
    i++;
  }
  return second.slice(i);
}
