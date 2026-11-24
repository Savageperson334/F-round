// slugify
//
// Copied verbatim from https://github.com/willianantunes/rave-of-phonetics
//   file frontend/src/utils/general.js, line 15
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Languages scripts and morphology
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function slugify(word, separator = "-") {
  return (
    word
      .toString()
      // split an accented letter in the base letter and the acent
      .normalize("NFD")
      // Remove all previously split accents
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .trim()
      // remove all chars not letters, numbers and spaces (to be replaced)
      .replace(/[^a-z0-9 ]/g, "")
      .replace(/\s+/g, separator)
  )
}
