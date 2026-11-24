// pixelEditorMoveFrame
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/actions/pixelEditor.js, line 70
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const PIXEL_EDITOR_MOVE_FRAME = 'PIXEL_EDITOR_MOVE_FRAME'


const pixelEditorMoveFrame = (srcIdx, targetIdx) => ({
  type: PIXEL_EDITOR_MOVE_FRAME,
  srcIdx,
  targetIdx
})
