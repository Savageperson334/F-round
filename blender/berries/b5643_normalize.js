// normalize
//
// Copied verbatim from https://github.com/qiyueblues/zhuomianling
//   file scripts/update-release-metadata.mjs, line 10
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Obscure computers, languages, unusual interfaces
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const normalize = (text) => text.replace(/\r\n/g, "\n").trim();
