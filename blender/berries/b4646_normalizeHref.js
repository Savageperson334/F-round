// normalizeHref
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file origami/src/dev/crawler/utilities.js, line 111
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function normalizeHref(href) {
  // Remove everything after a `#` or `?` character.
  const normalized = href.split(/[?#]/)[0];
  return normalized === "" ? null : normalized;
}
