// range
//
// Copied verbatim from https://github.com/YaseenHQ/Shipwreck
//   file scripts/editor-context-check.js, line 33
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Shipwrecks and maritime ghosts
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const range = (sl, sc, el, ec) => ({
  start: { line: sl, character: sc }, end: { line: el, character: ec },
  contains(p) {
    return (p.line > sl || p.line === sl && p.character >= sc)
      && (p.line < el || p.line === el && p.character <= ec);
  },
});
