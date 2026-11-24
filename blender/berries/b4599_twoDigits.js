// twoDigits
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file async-tree/src/drivers/CalendarMap.js, line 197
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function twoDigits(number) {
  return number.toString().padStart(2, "0");
}
