// timelineLayout
//
// Copied verbatim from https://github.com/Chienlin1014/Orrery
//   file timeline.js, line 209
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


function timelineLayout(width, height, rowCount) {
  const { left, right, top, bottom } = TIMELINE_PADDING;
  const plotWidth = Math.max(width - left - right, 1);
  const available = Math.max(height - top - bottom, 1);
  const pitch = rowCount > 0 ? Math.min(ROW_HEIGHT + ROW_GAP, available / rowCount) : 0;
  const barHeight = Math.max(pitch - ROW_GAP, 6);
  return {
    left, right, top, bottom, plotWidth, pitch, barHeight,
    rowY: (index) => top + index * pitch,
  };
}
