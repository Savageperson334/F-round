// normalizeReleasePath
//
// Copied verbatim from https://github.com/qiyueblues/zhuomianling
//   file scripts/release-asset-policy.mjs, line 45
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Obscure computers, languages, unusual interfaces
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function normalizeReleasePath(filePath) {
  return `/${String(filePath).replace(/\\/g, "/").replace(/^\/+/, "").toLowerCase()}`;
}
