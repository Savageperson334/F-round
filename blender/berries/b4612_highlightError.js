// highlightError
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file language/src/runtime/errors.js, line 109
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function highlightError(text) {
  // ANSI escape sequence to highlight text in red
  return `\x1b[31m${text}\x1b[0m`;
}
