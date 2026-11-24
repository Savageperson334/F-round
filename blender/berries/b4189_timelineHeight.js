// timelineHeight
//
// Copied verbatim from https://github.com/Chienlin1014/Orrery
//   file timeline.js, line 222
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const TIMELINE_PADDING = {
  left: 62, right: 12, top: 10, bottom: 22,
};

const ROW_HEIGHT = 22;

const ROW_GAP = 4;


function timelineHeight(rowCount) {
  return TIMELINE_PADDING.top + TIMELINE_PADDING.bottom + rowCount * (ROW_HEIGHT + ROW_GAP);
}
