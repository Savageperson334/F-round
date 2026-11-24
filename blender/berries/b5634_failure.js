// failure
//
// Copied verbatim from https://github.com/qiyueblues/zhuomianling
//   file scripts/oss-publisher.mjs, line 15
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Obscure computers, languages, unusual interfaces
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const failure = (code) => Object.assign(new Error(code), { code });
