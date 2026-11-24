// isbnCheckDigit
//
// Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
//   file legacy_library/server.js, line 39
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Archaeology & digital heritage
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function isbnCheckDigit(twelve) {
  let sum = 0;
  for (let k = 0; k < twelve.length; k++) {
    sum += Number(twelve[k]) * (k % 2 === 0 ? 1 : 3);
  }
  return String((10 - (sum % 10)) % 10);
}
