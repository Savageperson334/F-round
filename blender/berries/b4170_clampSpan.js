// clampSpan
//
// Copied verbatim from https://github.com/Chienlin1014/Orrery
//   file explainer.js, line 33
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function clampSpan(el, startJd, endJd) {
  const range = el.validRange;
  if (!range) return { startJd, endJd };
  return {
    startJd: Math.max(startJd, range.startJd),
    endJd: Math.min(endJd, range.endJd),
  };
}
