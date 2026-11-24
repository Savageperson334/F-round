// isOrigamiFrontMatter
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file language/src/compiler/isOrigamiFrontMatter.js, line 25
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function isOrigamiFrontMatter(text) {
  return /^[ \t\r\n]*[A-Za-z0-9_]*[\(\.\/\{<=]/.test(text);
}
