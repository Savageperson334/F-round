// toUri
//
// Copied verbatim from https://github.com/YaseenHQ/Shipwreck
//   file scripts/vscode-shim.js, line 34
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Shipwrecks and maritime ghosts
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const toUri = (p) => ({
  fsPath: p,
  scheme: "file",
  toString: () => "file:///" + String(p).replace(/\\/g, "/"),
  with: (x) => toUri(x && x.path !== undefined ? x.path : p),
});
