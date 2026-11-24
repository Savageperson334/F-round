// sliceData
//
// Copied verbatim from https://github.com/JamelSyh/braille-translator
//   file frontend/braille-translator/src/hooks/useTable.js, line 13
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Braille and tactile information
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const sliceData = (data, page, rowsPerPage) => {
  return data.slice((page - 1) * rowsPerPage, page * rowsPerPage);
};
