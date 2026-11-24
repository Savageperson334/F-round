// roundEven
//
// Copied verbatim from https://github.com/marksweiss/tastywaves
//   file tools/web/convert.js, line 17
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function roundEven(x) {                  // numpy's round: halves go to the even neighbour
  const r = Math.round(x);
  return (Math.abs(x % 1) === 0.5 && r % 2 !== 0) ? r - 1 : r;
}
